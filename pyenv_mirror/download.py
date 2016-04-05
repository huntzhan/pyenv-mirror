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
