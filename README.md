 - used Unstructured library (img ocr)

Extract data from unstructured PDF


Pyenv install
python 3.9.13

Install pyenv-win in PowerShell.

Type shell:

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"


1. Reopen PowerShell
2. Run pyenv --version to check if the installation was successful.
3. Run pyenv install -l to check a list of Python versions supported by pyenv-win
4. Run pyenv install <version> to install the supported version
5. Run pyenv global <version> to set a Python version as the global version
python -m venv .venv

6. .venv/Scripts/activate

7.  Set-ExecutionPolicy RemoteSigned -Scope Process

8. pip install unstructured
pip install "unstructured[pdf]"
