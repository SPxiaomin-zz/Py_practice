#!/usr/bin/env python
# _*_ coding: utf-8 _*_


'''
    Problem 0008 reference code.
'''


import re
import urllib.request


def get(url):
    html = urllib.request.urlopen(url).read()
    
    try:
        content = html.decode('utf-8')
    except UnicodeDecodeError:
        content = html.decode('gbk')
    
    r = re.compile(r'<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')

    result = r.findall(content)
    
    return result 

if __name__ == '__main__':
    url = input('Please input the url: ')

    body = get(url)

    file_object = open('result.txt', 'w')

    for i in body:
        file_object.write(i + '\n')

    file_object.close()
