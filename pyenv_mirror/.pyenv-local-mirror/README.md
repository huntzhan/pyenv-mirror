# Usage

Use `pyenv-mirror download-package` to download files to `./pythons`, then run
`./pythons/update.sh`.

```
# Usage:
#
# 1. Modify `./index.html` and add an entry for archive you want to add.
#    You can omit the sha256sum for the archive this time.
# 2. Download the archive from origin and save it in `./source`
# 3. Run `./update.sh`
# 4. Check diff of `./index.html` if the checksum is calculated properly
# 5. Commit files with name of `md5sum` and `sha256sum` of the archive
# 6. Push changes to the origin
```

Run service:

1. Define your `PYTHON_BUILD_MIRROR_URL` in `./pythons/install-pyenv.sh`.
2. Customize HTTP port by changing `PORT` of `./pythons/run-http-server.sh`. By
   default, `PORT` equals to `8999`.
3. Execute script `./pythons/run-http-server.sh`. 
