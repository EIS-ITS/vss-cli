class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/9f/b1/e9cbb5c0a9273c432f8117f14ea7c0aa2b091a08d8b8af553819b08dc663/vss_cli-2025.10.0-py2.py3-none-any.whl"
  sha256 "79b79c06baecb000630011c490c8044c560632cde1d4506156aa4d54464fecc8"
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