#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from HTMLParser import HTMLParser
import urllib2

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.link = []
    
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            if len(attrs) == 0:
                pass
            else:
                for variable, value in attrs:
                    if variable == "href":
                        self.link.append(value)

if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    html_txt = urllib2.urlopen(url).read()
    hp = MyHTMLParser()
    hp.feed(html_txt)
    hp.close()
    print(hp.link)
