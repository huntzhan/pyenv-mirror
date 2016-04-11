#!/usr/bin/env bash
#
# A script to generate md5sum/sha256sum files and index.html
#
# Usage:
#
# 1. Modify `./index.html` and add an entry for archive you want to add.
#    You can omit the sha256sum for the archive this time.
# 2. Download the archive from origin and save it in `./source`
# 3. Run `./update.sh`
# 4. Check diff of `./index.html` if the checksum is calculated properly
# 5. Commit files with name of `md5sum` and `sha256sum` of the archive
# 6. Push changes to the origin
#

set -e
set -x

compute_sha2() {
  local output
  if type shasum &>/dev/null; then
    output="$(shasum -a 256 -b)" || return 1
    echo "${output% *}"
  elif type openssl &>/dev/null; then
    output="$(openssl dgst -sha256)" || return 1
    echo "${output##* }"
  elif type sha256sum &>/dev/null; then
    output="$(sha256sum --quiet)" || return 1
    echo "${output% *}"
  else
    return 1
  fi
}

compute_md5() {
  local output
  if type md5 &>/dev/null; then
    md5 -q
  elif type openssl &>/dev/null; then
    output="$(openssl md5)" || return 1
    echo "${output##* }"
  elif type md5sum &>/dev/null; then
    output="$(md5sum -b)" || return 1
    echo "${output% *}"
  else
    return 1
  fi
}

for file in source/*; do
  base="$(basename "$file")"
  md5="$(compute_md5 < "$file")"
  sha="$(compute_sha2 < "$file")"
  ln -f "$file" "$md5"
  ln -f "$file" "$sha"
  sed -i -e "/>$base</s/^.*$/<li><a href=\"$sha\">$base<\/a><\/li>/" index.html
done

# vim:set ft=sh :
