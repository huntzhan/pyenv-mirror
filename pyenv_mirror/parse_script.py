import re
from urllib.parse import urlparse


def extract_filename(parsed_url):
    return parsed_url.path.split('/')[-1]


# return list of (url, filename)
def extract_urls(path):
    with open(path) as f:
        content = f.read()

    url_re = r'install_\S+?\s+"\S+?"\s+"(\S+?)"'

    url_filename = []
    for url in re.findall(url_re, content):
        parsed_url = urlparse(url)
        url_filename.append(
            (url, extract_filename(parsed_url)),
        )

    return url_filename
