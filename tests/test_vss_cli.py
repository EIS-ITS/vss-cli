import unittest
import os
import datetime
import pytz
from click.testing import CliRunner
import vss_cli.cli as cli
from vss_cli.const import __version__

import click_log.core as logcore


logcore.basic_config()


class TestVssCLI(unittest.TestCase):

    def setUp(self):
        self.test_folder = os.environ.get('VSS_API_TEST_FOLDER')
        self.test_network = os.environ.get('VSS_API_TEST_NETWORK')
        self.timestamp_dt = datetime.datetime.now(pytz.timezone('US/Eastern'))
        self.timestamp = self.timestamp_dt.strftime('%Y%d%M%H%M%S')
        self.timestamp_snap = self.timestamp_dt.strftime('%Y-%m-%d %H:%M')

    @classmethod
    def setUpClass(cls):
        super(TestVssCLI, cls).setUpClass()
        # setting up the CLI
        cls.runner = CliRunner()
        # Setting up credentials and endpoint
        cls.vss_api_user = os.environ.get('_VSS_API_USER')
        cls.vss_api_pass = os.environ.get('_VSS_API_USER_PASS')
        cls.vss_api_endpoint = os.environ.get('_VSS_API_ENDPOINT')
        cls.vss_api_endpoint_alt = os.environ.get('_VSS_API_ENDPOINT_ALT')
        r = cls.runner.invoke(
            cli.cli,
            ['--username', cls.vss_api_user,
             '--password', cls.vss_api_pass,
             '--server', cls.vss_api_endpoint,
             'configure', 'mk',
             '--replace'],
            catch_exceptions=False
        )
        assert r.exit_code == 0
        print(r.output.encode())

    def test_version(self):
        result = self.runner.invoke(
            cli.cli, ['--version'],
            catch_exceptions=False)
        self.assertEqual(result.exit_code, 0)
        assert __version__ in result.output

    def test_vss_shell(self):
        result = self.runner.invoke(
            cli.cli,
            ['shell'], input=':q\n',
            catch_exceptions=False
        )
        self.assertIn('history', result.output)
        self.assertEqual(result.exit_code, 0)
        result = self.runner.invoke(
            cli.cli,
            ['shell', '--history',
             '~/vss-cli/history'], input=':q\n',
            catch_exceptions=False
        )
        self.assertIn('History', result.output)
        self.assertEqual(result.exit_code, 0)

    def test_account_get_personal(self):
        result = self.runner.invoke(
            cli.cli,
            ['--server', self.vss_api_endpoint,
             'account', 'get', 'personal'],
            catch_exceptions=False
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn('USERNAME', result.output)
