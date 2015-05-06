#!/usr/bin/env python3

# _*_ coding: UTF-8 _*_



import random

import string



def rand_str(num, length = 7):

    f = open('activation_code.txt', 'w')

    for i in range(num):

        chars = string.ascii_letters + string.digits;

        s = [random.choice(chars) for i in range(length)]

        f.write(str(i) + ' ' + ''.join(s) + '\n')

    f.close()

    return 0



num = int(input('Please input the number of activation code: '))

rand_str(num)
