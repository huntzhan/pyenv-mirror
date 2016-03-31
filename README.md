# Introduction

Help building a pyenv local mirror!

`pyenv-mirror-download` would download all related files of a package to current working directory:

```
$ pyenv-mirror-download 2.7 '/usr/local/Cellar/pyenv/20160310/plugins/python-build/share/python-build'
Downloading https://www.openssl.org/source/openssl-1.0.2g.tar.gz#b784b1b3907ce39abf4098702dade6365522a253ad1552e267a9a0e89594aa33
Downloading http://ftpmirror.gnu.org/readline/readline-6.3.tar.gz#56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43
Downloading http://www.python.org/ftp/python/2.7/Python-2.7.tgz#5670dd6c0c93b0b529781d070852f7b51ce6855615b16afcd318341af2910fb5
$ ls
Python-2.7.tgz        openssl-1.0.2g.tar.gz readline-6.3.tar.gz
```

# Install

```
pip install pyenv-mirror-download
```

# Usage

```
$ pyenv-mirror-download --help                                                                
Usage:
    pyenv-mirror-download <pkg-name> [<python-build-path>]
```

* `<pkg-name>`, same as the arguement following `pyenv install`.
* `<python-build-path>`, the path of [python-build][1] directory. If you install `pyenv` by using homebrew, you might need to pass the path of above directory explicitly. If omitted, the path is default to `$PYENV_ROOT/plugins/python-build/share/python-build`.

[1]: https://github.com/yyuu/pyenv/tree/master/plugins/python-build/share/python-build

