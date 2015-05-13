#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import os

def get_files(path):
    file_or_dir_name = os.listdir(path)

    files = []

    for name in file_or_dir_name:
        f_path = path + '/' + name

        if os.path.isfile(f_path):
            files.append(f_path)
        elif os.path.isdir(f_path):
            files += get_files(f_path)

    return files

def count_lines(files):
    line, black, note = 0, 0, 0
    
    for file in files:
        with open(file) as f:
            for one_line in f:
                one_line = one_line.strip()
                line += 1
                if one_line == '':
                    black += 1
                elif one_line[0] == '#' or one_line[0] == '/':
                    note += 1

    return line, black, note

if __name__ == '__main__':
    files = get_files('.')

    lines = count_lines(files)

    print('Line(s): %d, black line(s): %d, note(s): %d' % ( lines[0], lines[1], lines[2] ))
