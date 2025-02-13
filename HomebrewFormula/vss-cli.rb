class VssCli < Formula
  include Language::Python::Virtualenv

  desc "ITS Private Cloud Command Line Interface vss-cli"
  homepage "https://eis.utoronto.ca/~vss/vss-cli"
  url "https://files.pythonhosted.org/packages/95/d7/fd779cdff1120e3d2adccba492270b8b3fb15ef01898d00c0a9920fbf114/vss_cli-2025.2.0-py2.py3-none-any.whl"
  sha256 "7011ec1e422a621451c1664cd7e475b1383b929d65cee6cad6570ee5cf36b7b5"
  license "MIT"

  depends_on "python@3.11"
  depends_on "pipx" => :build
  depends_on "rust" => :build

  def install
    ENV["PIPX_HOME"] = prefix
    ENV["PIPX_BIN_DIR"] = bin
    ENV["PIPX_DEFAULT_PYTHON"] = Formula["python@3.11"].opt_bin/"python3.11"

    whl_file = "vss_cli-2024.10.0-py2.py3-none-any.whl"
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