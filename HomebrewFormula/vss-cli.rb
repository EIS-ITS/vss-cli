class VssCli < Formula

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/0c/14/2515b48b8f40af971ac426354a1f594bc76b3c90a0071324077a84744f43/vss_cli-2023.6.0-py2.py3-none-any.whl"
  sha256 "6906c5f677d4ff3aa79f9d5bab2f5a2ed9234e11ac632c64e312c4dd420f36dd"
  license "MIT"

  depends_on "python@3.10"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.10"].opt_bin/"python3"

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