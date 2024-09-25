class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/b8/ab/326f6ddb9c198cf92a4887fc81803a3943e5586cec8c505a654c3c52f249/vss_cli-2024.9.0-py2.py3-none-any.whl"
  sha256 "f3634db61c0db201751d74e46172ec79b657556a0451553bf26227d1e48509b2"
  license "MIT"

  depends_on "python@3.11"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.11"].opt_bin/"python3.11"

    system "pipx install ./*.whl"

    (bash_completion/"vss_cli").write `#{bin}/vss-cli completion bash`
    (fish_completion/"vss_cli.fish").write `#{bin}/vss-cli completion fish`
    (zsh_completion/"_vss_cli").write `#{bin}/vss-cli completion zsh`
  end

  test do
    # `test do` will create, run in and delete a temporary directory.
    #
    # This test will fail and we won't accept that! For Homebrew/homebrew-core
    # this will need to be a test that verifies the functionality of the
    # software. Run the test with `brew test uoft_switchconfig`. Options passed
    # to `brew install` such as `--HEAD` also need to be provided to `brew test`.
    #
    # The installed folder is not in the path, so use the entire path to any
    # executables being tested: `system "#{bin}/program", "do", "something"`.
    system "#{bin}/vss-cli", "--help"
  end
end