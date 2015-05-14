#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import re
import urllib

def get_html(url):
    page = urllib.urlopen(url)
    
    html = page.read()
    
    return html

def download_pic(html):
    r = re.compile(r'src="(.+?\.jpg)"')

    img_infos = r.findall(html)

    i = 1
    for img_info in img_infos:
        urllib.urlretrieve(img_info, "%s.jpg" % i )

        i += 1

    return

if __name__ == '__main__':
    html = get_html('http://desk.zol.com.cn/bizhi/5418_67006_2.html')
    download_pic(html)
