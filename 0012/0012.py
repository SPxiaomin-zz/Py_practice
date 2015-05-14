#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


import re

def readFile(filename):
    lines = []
    
    with open(filename) as file:
        for line in file:
            lines.append(line.strip())
    
    return lines

def create_pattern(lines):
    pattern = ''

    for line in lines:
        pattern += line + '|'

    return pattern[:-1]

def replace(pattern):
    string = input('Please input a sentence: ')
    return re.sub(pattern, '**', string)

if __name__ == '__main__':
    lines = readFile('./filtered_words.txt')
    pattern = create_pattern(lines)
    print(replace(pattern))
