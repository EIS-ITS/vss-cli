class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/22/41/ddb2cba21c7a3a4c3b55566c79fe71f8e62ed2b75872ae925c721a522e71/vss_cli-2026.4.0-py2.py3-none-any.whl"
  sha256 "86759eeb8991e17472ea2c23f09993e3e0c29c13aa7baf372fd557a88cf48254"
  license "MIT"

  depends_on "python@3.11"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.11"].opt_bin/"python3.11"

    whl_file = File.basename(self.class.url)
    system "pipx", "install", "#{whl_file}[mcp,stor]"
    system "pipx", "inject", "vss-cli", "mcp-vss"

    (bash_completion/"vss_cli").write `#{bin}/vss-cli completion bash`
    (fish_completion/"vss_cli.fish").write `#{bin}/vss-cli completion fish`
    (zsh_completion/"_vss_cli").write `#{bin}/vss-cli completion zsh`
  end

  test do
    # Test basic functionality
    system "#{bin}/vss-cli", "--help"
    system "#{bin}/vss-cli", "--version"
  end
end