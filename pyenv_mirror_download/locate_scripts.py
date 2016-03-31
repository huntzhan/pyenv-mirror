import os


# return the valid path of python-build/share/python-build, None otherwise.
def check_directory(path=None):
    if path is None:
        # try to guess.
        pyenv_root = os.environ.get('PYENV_ROOT', None)
        if pyenv_root:
            path = os.path.join(
                pyenv_root,
                'plugins/python-build/share/python-build',
            )

    if path is None or not os.path.isdir(path):
        return None

    # small hack.
    test_script_path = os.path.join(
        path,
        '2.7',
    )
    if os.path.isfile(test_script_path):
        return path
    else:
        return None


# return the valid path of target script, None otherwise.
def check_script(script_dir_path, script_name):
    path = os.path.join(
        script_dir_path,
        script_name,
    )
    if os.path.isfile(path):
        return path
    else:
        return None
