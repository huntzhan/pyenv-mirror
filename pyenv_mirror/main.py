#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import os

from docopt import docopt

from pyenv_mirror.metadata import VERSION
from pyenv_mirror.locate_scripts import (
    check_directory,
    check_script,
)
from pyenv_mirror.parse_script import (
    extract_urls,
)
from pyenv_mirror.download import (
    download_source_package,
)


DOC = '''
Usage:
    pyenv-mirror create-mirror
    pyenv-mirror download <pkg-name> [<python-build-path>]
    pyenv-mirror start [--port=<PORT>]
'''


def entry_point():
    args = docopt(DOC, version=VERSION)
    pkg_name = args['<pkg-name>']
    python_build_path = args['<python-build-path>'] or None

    # init.
    target_dir_path = check_directory(python_build_path)
    if target_dir_path is None:
        print("Invalid Target Dir.")
        return 1

    script_path = check_script(target_dir_path, pkg_name)
    if script_path is None:
        print("Invalid Pkg Name.")
        return 1

    # extract related packages.
    url_filename = extract_urls(script_path)
    for url, filename in url_filename:
        if os.path.exists(filename):
            print("{} already exists.".format(filename))
            continue

        binary = download_source_package(url)
        with open(filename, 'wb') as f:
            f.write(binary)

    return 0
