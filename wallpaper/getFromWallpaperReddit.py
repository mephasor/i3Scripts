#!/usr/bin/python3.5

import urllib.request
import xml.etree.ElementTree as ET
import re
import subprocess

def setAsWallpaper(url):
    subprocess.call("feh --bg-scale "+url, shell=True)

def getImgUrl(content):
    p = re.compile('<\/a> <br\/> <span><a href="(.*)">\[link\]')
    result = re.search(p, content)
    return(result.groups()[0])

def getPostContent(xmlContent):
    root = ET.fromstring(xmlContent)
    # Some magic numbers to get the first post in the feed
    post = root[9][2].text
    return post

def main():
    src = 'https://www.reddit.com/r/wallpaper/.rss'
    req = urllib.request.Request(
        src,
        data=None,
        headers={'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3)'
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47'
                               'Safari/537.36')}
    )
    with urllib.request.urlopen(req) as response:
        xml = response.read()
        content = getPostContent(xml)
        url = getImgUrl(content);
        setAsWallpaper(url)

if __name__ == "__main__":
    main()
