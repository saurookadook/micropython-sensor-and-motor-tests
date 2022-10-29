# Lego EV3 Projects

## General

- [Connecting to EV3dev Using SSH](https://www.ev3dev.org/docs/tutorials/connecting-to-ev3dev-with-ssh/)

```bash
$ ssh robot@ev3dev.local
```
_default password is `maker`_

## [Code Completion](https://github.com/ev3dev/vscode-hello-python#code-completion)
_from [ev3dev/vscode-hello-python](https://github.com/ev3dev/vscode-hello-python)_

To get code completion working and fix errors like "Unable to import 'ev3dev2.motor'" you will need to install Python and the python-ev3dev package on your computer.

If you don't already have Python installed, get it from https://python.org or your favorite package manager (Chocolaty, Homebrew, Apt, etc.).

Then set up a virtual environment. You can type these commands on the built-in terminal in VS Code.

On Windows (make sure you are using CMD, not PowerShell):

```powershell
py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install python-ev3dev2
```

Or non-Windows:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install python-ev3dev2
```

In the VS Code command pallete, run the Python: Select Interpreter command to select the .venv folder that you just created.

---

### Initial Setup

Turn on brick and _**make sure it's connected to the internet**_

- SSH into brick
- add python3 alias to `.bashrc` using `vim`
```shell
$ vim ~/.bashrc
# edit file
$ :w # and press enter to write changes
$ :q # and press enter to exit vim
```

### Resources

- [Getting Started with ev3dev](https://www.ev3dev.org/docs/getting-started/)
- [Programming Languages for EV3](https://www.ev3dev.org/docs/programming-languages/)
  - [Python language bindings for ev3dev](https://github.com/ev3dev/ev3dev-lang-python)
