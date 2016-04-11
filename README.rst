Introduction
============

Help building a pyenv local mirror!

Install
=======

::

    pip install pyenv-mirror

Usage
=====

::

    $ pyenv-mirror-download --help                                                                
    Usage:
        pyenv-mirror create-mirror
        pyenv-mirror download-package <pkg-name> [<python-build-path>]

``create-mirror``
-----------------

::

    $ ls
    $ pyenv-mirror create-mirror
    $ ls
    pyenv-local-mirror

Create a directory named ``pyenv-local-mirror`` in current working
directory. The structure of ``pyenv-local-mirror`` is almost identical
to `yyuu/yyuu.github.com <https://github.com/yyuu/yyuu.github.com>`__,
except that all the so-called "packages" located in
``pyenv-local-mirror/pythons`` were removed.

``download-package``
--------------------

``pyenv-mirror download-package`` downloads all related files of a
package to current working directory.
``pyenv-mirror download-package <pkg-name> [<python-build-path>]``:

-  ``<pkg-name>``, same as the arguement following ``pyenv install``.
-  ``<python-build-path>``, the path of
   `python-build <https://github.com/yyuu/pyenv/tree/master/plugins/python-build/share/python-build>`__
   directory. If you installed ``pyenv`` through homebrew, you might
   need to pass the path of above directory explicitly. If omitted, the
   path is default to
   ``$PYENV_ROOT/plugins/python-build/share/python-build``.

::

    $ pyenv-mirror download-package 2.7 '/usr/local/Cellar/pyenv/20160310/plugins/python-build/share/python-build'
    Downloading https://www.openssl.org/source/openssl-1.0.2g.tar.gz#b784b1b3907ce39abf4098702dade6365522a253ad1552e267a9a0e89594aa33
    Downloading http://ftpmirror.gnu.org/readline/readline-6.3.tar.gz#56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43
    Downloading http://www.python.org/ftp/python/2.7/Python-2.7.tgz#5670dd6c0c93b0b529781d070852f7b51ce6855615b16afcd318341af2910fb5
    $ ls
    Python-2.7.tgz        openssl-1.0.2g.tar.gz readline-6.3.tar.gz

Start The Mirror
----------------

#. ``cd pyenv-local-mirror``.
#. Define your ``PYTHON_BUILD_MIRROR_URL`` in
   ``./pythons/install-pyenv.sh``.
#. Customize HTTP port by changing ``PORT`` of
   ``./pythons/run-http-server.sh``. By
   default, ``PORT`` equals to ``8999``.
#. Execute script ``./pythons/run-http-server.sh``.
