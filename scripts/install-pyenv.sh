#!/usr/bin/env bash

PYTHON_BUILD_MIRROR_URL=''
OFFLINE_INSTALL_SCRIPT='pyenv-offline-installer'
PYENV_PACKAGE='pyenv-package.tar.gz'

TMP_DIR=$(mktemp -d)

# download files.
wget "$PYTHON_BUILD_MIRROR_URL/$OFFLINE_INSTALL_SCRIPT" -P "$TMP_DIR"
wget "$PYTHON_BUILD_MIRROR_URL/$PYENV_PACKAGE" -P "$TMP_DIR"

# install.
chmod +x "$TMP_DIR/$OFFLINE_INSTALL_SCRIPT"
bash "$TMP_DIR/$OFFLINE_INSTALL_SCRIPT"
