class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/7e/0f/b7107620d99ccf1033f381ba363f5f1b9080559c993177efe506a2b5e4bf/vss_cli-2025.2.1-py2.py3-none-any.whl"
  sha256 "3e90a9c397fc0cabe60eb170b0a6deb91fbe86f26cb882a1007f92b0291f3549"
  license "MIT"

  depends_on "python@3.11"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.11"].opt_bin/"python3.11"

    whl_file = "vss_cli-2025.2.1-py2.py3-none-any.whl"
    system "pipx", "install", "#{whl_file}[stor]"

    (bash_completion/"vss_cli").write `#{bin}/vss-cli completion bash`
    (fish_completion/"vss_cli.fish").write `#{bin}/vss-cli completion fish`
    (zsh_completion/"_vss_cli").write `#{bin}/vss-cli completion zsh`
  end

  test do
    # `test do` will create, run in and delete a temporary directory.
    # The installed folder is not in the path, so use the entire path to any
    # executables being tested: `system "#{bin}/program", "do", "something"`.
    system "#{bin}/vss-cli", "--help"
  end
end