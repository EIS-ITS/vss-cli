"""Tests for GPU profile support in VM creation commands."""

import unittest
from unittest.mock import patch

from click.testing import CliRunner

import vss_cli.cli as cli
from vss_cli.plugins.compute_plugins.vm import (
    compute_vm_mk_clib,
    compute_vm_mk_clone,
    compute_vm_mk_image,
    compute_vm_mk_shell,
    compute_vm_mk_spec,
    compute_vm_mk_template,
)


class TestVmMkGpuProfileRegistration(unittest.TestCase):
    """Verify --gpu-profile option is registered on all mk commands."""

    COMMANDS = {
        'from-template': compute_vm_mk_template,
        'from-clone': compute_vm_mk_clone,
        'from-clib': compute_vm_mk_clib,
        'shell': compute_vm_mk_shell,
        'from-image': compute_vm_mk_image,
        'from-spec': compute_vm_mk_spec,
    }

    def _get_param(self, cmd, name):
        """Get a Click parameter by name from a command."""
        for p in cmd.params:
            if p.name == name:
                return p
        return None

    def test_all_commands_have_gpu_profile_param(self):
        """All six mk commands must have gpu_profile parameter."""
        for cmd_name, cmd in self.COMMANDS.items():
            param = self._get_param(cmd, 'gpu_profile')
            self.assertIsNotNone(
                param,
                f'{cmd_name} is missing gpu_profile parameter',
            )

    def test_gpu_profile_is_optional(self):
        """--gpu-profile must be optional on all commands."""
        for cmd_name, cmd in self.COMMANDS.items():
            param = self._get_param(cmd, 'gpu_profile')
            self.assertFalse(
                param.required,
                f'{cmd_name}: --gpu-profile should not be required',
            )

    def test_gpu_profile_is_multiple(self):
        """--gpu-profile must accept multiple values."""
        for cmd_name, cmd in self.COMMANDS.items():
            param = self._get_param(cmd, 'gpu_profile')
            self.assertTrue(
                param.multiple,
                f'{cmd_name}: --gpu-profile should be multiple',
            )

    def test_gpu_profile_option_name(self):
        """--gpu-profile must use the long option name."""
        for cmd_name, cmd in self.COMMANDS.items():
            param = self._get_param(cmd, 'gpu_profile')
            self.assertIn(
                '--gpu-profile',
                param.opts,
                f'{cmd_name}: option should use --gpu-profile',
            )

    def test_gpu_profile_has_help_text(self):
        """--gpu-profile must have help text."""
        for cmd_name, cmd in self.COMMANDS.items():
            param = self._get_param(cmd, 'gpu_profile')
            self.assertIsNotNone(
                param.help,
                f'{cmd_name}: --gpu-profile should have help text',
            )
            self.assertIn(
                'GPU',
                param.help,
                f'{cmd_name}: help text should mention GPU',
            )


class TestVmMkGpuProfilePayload(unittest.TestCase):
    """Test GPU profile resolution and payload construction."""

    @classmethod
    def setUpClass(cls):
        """Set up test runner."""
        super().setUpClass()
        cls.runner = CliRunner()

    @patch('vss_cli.plugins.compute_plugins.vm.format_output')
    @patch('vss_cli.config.Configuration.deploy_vm_from_template')
    @patch(
        'vss_cli.config.Configuration' '.get_vm_gpu_profiles_by_name_or_desc'
    )
    @patch('vss_cli.config.Configuration.get_vm_by_id_or_name')
    @patch('vss_cli.config.Configuration.load_config')
    def test_single_gpu_profile_from_template(
        self,
        mock_load,
        mock_get_vm,
        mock_gpu_lookup,
        mock_deploy,
        mock_fmt,
    ):
        """Single --gpu-profile resolves and passes gpus list."""
        mock_load.return_value = None
        mock_get_vm.return_value = [{'moref': 'vm-123'}]
        mock_gpu_lookup.return_value = [
            {
                'type': 'grid_v100d-4q',
                'description': 'NVIDIA V100D',
            }
        ]
        mock_deploy.return_value = {'_links': {'request': 'req-1'}}
        mock_fmt.return_value = 'ok'

        self.runner.invoke(
            cli.cli,
            [
                'compute',
                'vm',
                'mk',
                'from-template',
                '--source',
                'my-template',
                '--description',
                'GPU VM test',
                '--gpu-profile',
                'grid_v100d-4q',
                'test-vm',
            ],
            catch_exceptions=False,
        )

        mock_gpu_lookup.assert_called_once_with('grid_v100d-4q')
        call_kwargs = mock_deploy.call_args
        if call_kwargs:
            kwargs = call_kwargs[1] if call_kwargs[1] else {}
            self.assertIn('gpus', kwargs)
            self.assertEqual(kwargs['gpus'], ['grid_v100d-4q'])

    @patch('vss_cli.plugins.compute_plugins.vm.format_output')
    @patch('vss_cli.config.Configuration.deploy_vm_from_template')
    @patch(
        'vss_cli.config.Configuration' '.get_vm_gpu_profiles_by_name_or_desc'
    )
    @patch('vss_cli.config.Configuration.get_vm_by_id_or_name')
    @patch('vss_cli.config.Configuration.load_config')
    def test_multiple_gpu_profiles_from_template(
        self,
        mock_load,
        mock_get_vm,
        mock_gpu_lookup,
        mock_deploy,
        mock_fmt,
    ):
        """Multiple --gpu-profile flags produce a list."""
        mock_load.return_value = None
        mock_get_vm.return_value = [{'moref': 'vm-123'}]
        mock_gpu_lookup.side_effect = [
            [{'type': 'grid_v100d-4q', 'description': 'V100D'}],
            [{'type': 'grid_a100-10c', 'description': 'A100'}],
        ]
        mock_deploy.return_value = {'_links': {'request': 'req-1'}}
        mock_fmt.return_value = 'ok'

        self.runner.invoke(
            cli.cli,
            [
                'compute',
                'vm',
                'mk',
                'from-template',
                '--source',
                'my-template',
                '--description',
                'Multi GPU VM',
                '--gpu-profile',
                'grid_v100d-4q',
                '--gpu-profile',
                'grid_a100-10c',
                'test-vm',
            ],
            catch_exceptions=False,
        )

        self.assertEqual(mock_gpu_lookup.call_count, 2)
        call_kwargs = mock_deploy.call_args
        if call_kwargs:
            kwargs = call_kwargs[1] if call_kwargs[1] else {}
            self.assertIn('gpus', kwargs)
            self.assertEqual(
                kwargs['gpus'],
                ['grid_v100d-4q', 'grid_a100-10c'],
            )

    @patch('vss_cli.plugins.compute_plugins.vm.format_output')
    @patch('vss_cli.config.Configuration.deploy_vm_from_template')
    @patch('vss_cli.config.Configuration.get_vm_by_id_or_name')
    @patch('vss_cli.config.Configuration.load_config')
    def test_no_gpu_profile_omits_gpus_key(
        self,
        mock_load,
        mock_get_vm,
        mock_deploy,
        mock_fmt,
    ):
        """Omitting --gpu-profile keeps gpus out of payload."""
        mock_load.return_value = None
        mock_get_vm.return_value = [{'moref': 'vm-123'}]
        mock_deploy.return_value = {'_links': {'request': 'req-1'}}
        mock_fmt.return_value = 'ok'

        self.runner.invoke(
            cli.cli,
            [
                'compute',
                'vm',
                'mk',
                'from-template',
                '--source',
                'my-template',
                '--description',
                'No GPU VM',
                'test-vm',
            ],
            catch_exceptions=False,
        )

        call_kwargs = mock_deploy.call_args
        if call_kwargs:
            kwargs = call_kwargs[1] if call_kwargs[1] else {}
            self.assertNotIn('gpus', kwargs)


if __name__ == '__main__':
    unittest.main()
