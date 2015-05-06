#!/usr/bin/env python

#_*_ coding: UTF-8 _*_



import Image

import ImageDraw

import ImageFont



def add_num(img):

    font = ImageFont.truetype("/usr/share/fonts/truetype/tibetan-machine/TibetanMachineUni.ttf", 80)

    imgDraw = ImageDraw.Draw(img)

    width,height = img.size

    imgDraw.text((80, 1), "4", fill=(255, 0, 0), font=font)

    img.save("result.jpg", "jpeg")

    img.show()

    return 0



if __name__ == '__main__':

    img = Image.open("/home/gujunmin/Downloads/touxiang.png")

    add_num(img)
