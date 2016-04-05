import os
from pyenv_mirror.locate_scripts import (
    check_directory,
    check_script,
)
from pyenv_mirror.parse_script import (
    extract_filename,
    extract_urls,
)
from tests.env import TEST_DIR_PATH


TARGET_DIR_PATH = os.path.join(
    TEST_DIR_PATH,
    'test_pyenv_root/plugins/python-build/share/python-build',
)


def test_missing_path():
    os.environ['PYENV_ROOT'] = os.path.join(
        TEST_DIR_PATH,
        'test_pyenv_root',
    )
    assert TARGET_DIR_PATH == check_directory()


def test_normal_path():
    assert TARGET_DIR_PATH == check_directory(TARGET_DIR_PATH)
    assert check_directory(TEST_DIR_PATH) is None


def test_check_script():
    assert check_script(TARGET_DIR_PATH, '2.7')
    assert check_script(TARGET_DIR_PATH, '2.7.11')
    assert not check_script(TARGET_DIR_PATH, 'not-exists')


def test_extract_filename():
    from urllib.parse import urlparse

    url = (
        'http://www.python.org/ftp/python/2.7/Python-2.7.tgz'
        '#'
        '5670dd6c0c93b0b529781d070852f7b51ce6855615b16afcd318341af2910fb5'
    )
    parsed_url = urlparse(url)
    assert 'Python-2.7.tgz' == extract_filename(parsed_url)


def test_extract_2_7():
    path = os.path.join(
        TARGET_DIR_PATH,
        '2.7',
    )
    url_filename = extract_urls(path)
    assert [
        ('https://www.openssl.org/source/openssl-1.0.2g.tar.gz#b784b1b3907ce39abf4098702dade6365522a253ad1552e267a9a0e89594aa33',  # noqa
         'openssl-1.0.2g.tar.gz'),
        ('http://ftpmirror.gnu.org/readline/readline-6.3.tar.gz#56ba6071b9462f980c5a72ab0023893b65ba6debb4eeb475d7a563dc65cafd43',  # noqa
         'readline-6.3.tar.gz'),
        ('http://www.python.org/ftp/python/2.7/Python-2.7.tgz#5670dd6c0c93b0b529781d070852f7b51ce6855615b16afcd318341af2910fb5',  # noqa
         'Python-2.7.tgz'),
    ] == url_filename
