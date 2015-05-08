#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

def sensitiveWordsFromFile(filePath):
    words = []
    for i in open(filePath).readlines():
        words.append(i.strip('\n'))
    return words

def check(testword):
    for i in sensitiveWords:
        if i == testword:
            print 'Freedom'
            return
    else:
        print 'Human Rights'
        return

if __name__ == '__main__':
    sensitiveWords = sensitiveWordsFromFile('./filtered_words.txt')
    testword = raw_input('Please input the word you wanna to test: ')
    check(testword)
