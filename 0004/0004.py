#!/usr/bin/env python3

# _*_ coding: UTF-8 _*_



import re



def count_word_num():

    f = open("English.txt")

    words = f.read()

    result = re.findall(r"[a-zA-Z]+", words)

    print(result)

    print(len(result))

    return 0



if __name__ == '__main__':

    count_word_num()
