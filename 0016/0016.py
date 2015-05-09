#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import json
import xlwt

f = xlwt.Workbook(encoding = 'utf-8')

table = f.add_sheet('numbers')

txt = open('./numbers.txt').read()

json_txt = json.loads(txt)

for x in range(len(json_txt)):
    for y in range(len(json_txt[x])):
        table.write(x, y, json_txt[x][y])

f.save('numbers.xls')
