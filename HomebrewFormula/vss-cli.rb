class VssCli < Formula

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/c8/d9/b9b6c2dd53249da58ce45c21f9acc6360b6028c1082e7b8f37c819be38c5/vss_cli-2023.10.0-py2.py3-none-any.whl"
  sha256 "c789424966ef81e2604ed1f042af73d21f2f8bfb684e2dbf999253759bc76259"
  license "MIT"

  depends_on "python@3.10"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    # ENV.deparallelize  # if your formula fails when building in parallel
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.10"].opt_bin/"python3.10"

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