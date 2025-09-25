class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/6b/ee/6284ad938660288eb2584d6d5837a50a843634e33e6cc624b3a9b747419c/vss_cli-2025.9.0-py2.py3-none-any.whl"
  sha256 "5f6badb7a14ae8258d34ed989a2117d9bec5be1594a72ccf473f49866b38265d"
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