#!/usr/bin/env python
# _*_ coding: utf-8 _*_


import Image

def change_resolution(picPath, size = (1136, 640)):
    img = Image.open(picPath)
    img.thumbnail(size)
    img.save('result.jpg')

if __name__ == '__main__':
    change_resolution('./a.jpg', (1136, 640))
