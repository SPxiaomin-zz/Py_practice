#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import re
import os

def get_files(path):
    file_or_dir_name = os.listdir(path)
    
    files = []
    
    for f in file_or_dir_name:
        fpath = path + '/' + f
        if os.path.isfile(fpath):
            files.append(fpath)
        elif os.path.isdir(fpath):
            files += get_files(fpath)

    return files

def get_important_word_dict(files):
    word_dict = {}
    
    for f in files:
        with open(f) as fp:
            string = fp.read()
            words = re.findall(r'[a-zA-Z]+\b', string)
            
            for word in words:
                word_dict[word] = word_dict[word] + 1 if word in word_dict else 1
    
    word_sort = sorted(word_dict.items(), key = lambda e : e[1], reverse = True)
    
    return word_sort

if __name__ == '__main__':
    files = get_files('.')
    
    word_sort = get_important_word_dict(files)

    maxnum = 1

    for i in range(len(word_sort)-1):
        if word_sort[i][1] == word_sort[i+1][1]:
            maxnum += 1
        else:
            break

    for i in range(maxnum):
        print(word_sort[i])
