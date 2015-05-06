#!/usr/bin/env python

#_*_coding: UTF-8 _*_



import Image, ImageDraw, ImageFont, ImageFilter

import string

import random



def randChar():

    return random.choice(string.ascii_letters)



def randColor():

    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))



def randColor2():

    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))



def generate_authenticode():

    width = 60 * 4

    height = 60

    image = Image.new("RGB", (width, height), (255, 255, 255))



    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerifBold.ttf", 36)



    draw = ImageDraw.Draw(image)



    for x in range(width):

        for y in range(height):

            draw.point((x, y), fill = randColor())



    for i in range(4):

        draw.text((60 * i + 10, 10), randChar(), fill = randColor2(), font = font)



    image = image.filter(ImageFilter.BLUR)

    image.save('code.jpg', 'jpeg')



    return



if __name__ == '__main__':

    generate_authenticode()

