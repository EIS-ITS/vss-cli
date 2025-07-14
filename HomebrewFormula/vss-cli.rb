class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/51/45/1a6d505e3c94eb8f5f548bb563e5234148ee7d4ce82913cea714a0b32b3a/vss_cli-2025.7.0-py2.py3-none-any.whl"
  sha256 "21602d80c9558a2feff3eb799ef94b3cc4d8da864f3ddde66a3661e44e202670"
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