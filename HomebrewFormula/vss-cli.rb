class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/77/d5/3ab174fa32222950dc451afb8744200b97df02cdce2a0f3a39f2a8c520f0/vss_cli-2025.8.0-py2.py3-none-any.whl"
  sha256 "ad476bab2152fdc34a07734dc9ae39bf63d55ba7674a5325733441216e1d9120"
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