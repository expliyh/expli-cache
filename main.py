import os
import sys
import requests

page = 1

baseURL = "https://www.expli.top/wp-json/wp/v2/posts"

URLPath = "?categories=24"

rURL = ""


def get(per_page, page):
    base_url = "https://www.expli.top/wp-json/wp/v2/posts"
    url_path = "?categories=24"
    real_url = base_url + url_path
    real_url += "&per_page="
    real_url += str(per_page)
    real_url += "&page="
    real_url += str(page)
    respond0 = requests.get(real_url)
    return respond0


def write(perPage, page, text):
    toWrite = open("cache/" + str(perPage) + '/' + str(page) + ".json", "x")
    toWrite.write(text)
    toWrite.close()
    return

def lock():
    key=sys.argv[0]
    key="k"
    requests.post("https://apicache.expli.top/wp-json/wp/v2/posts/lock.php",data={"key":key})

lock()
os.system("rm -rf cache")
os.mkdir("cache")

respond = requests.get("https://www.expli.top/wp-json/wp/v2/posts?categories=24")
toWrite = open("cache/default.json", "x")
toWrite.write(respond.text)
toWrite.close()

for perPage in range(1, 50):
    os.mkdir("cache/" + str(perPage))
    while 1:
        respond = get(perPage, page)
        if respond.status_code == 400:
            page = 1
            break
        write(perPage, page, respond.text)
        page += 1
