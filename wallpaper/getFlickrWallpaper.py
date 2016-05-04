#!/usr/bin/python3.5

import urllib.request
import xml.etree.ElementTree as ET
import re
import subprocess

def setAsWallpaper(url):
    subprocess.call("feh --bg-scale "+url, shell=True)

def getImgUrl(content):
    root = ET.fromstring(content)
    # Some magic numbers to get the first post in the feed
    post = root[0][7][7].attrib['url']
    return post

def main():
    src = 'https://api.flickr.com/services/feeds/groups_pool.gne?id=40961104@N00&lang=en-us&format=rss_200'
    req = urllib.request.Request(
        src,
        data=None,
        headers={'User-Agen': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47'
                               'Safari/537.36')}
    )
    with urllib.request.urlopen(req) as response:
        xml = response.read()
        url = getImgUrl(xml);
        setAsWallpaper(url)

if __name__ == "__main__":
    main()
