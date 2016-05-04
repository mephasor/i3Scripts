#!/usr/bin/python3.5

import urllib.request
import re
import subprocess

def setAsWallpaper(url):
    subprocess.call("feh --bg-scale "+url, shell=True)

def getImgUrl(content):
    pattern = '"url":"(.*)","url';
    p = re.compile(pattern)
    result = re.search(p, content)
    return('http://www.bing.com/'+result.groups()[0])


def main():
    src = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'
    req = urllib.request.Request(
        src,
        data=None,
        headers={'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47'
                               'Safari/537.36')}
    )
    with urllib.request.urlopen(req) as response:
        content = response.read()
        url = getImgUrl(str(content));
        # print(url)
        setAsWallpaper(url)

if __name__ == "__main__":
    main()
