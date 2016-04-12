# -*- coding: utf-8 -*-
from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import requests


def download_source_package(url):
    retry = 3
    print('Downloading {}'.format(url))
    while retry > 0:
        try:
            r = requests.get(url)
            break
        except requests.exceptions.RequestException:
            print('Error. Retry.')
            retry -= 1

    return r.content
