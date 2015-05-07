#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import xlwt
import json

file = xlwt.Workbook(encoding = 'utf-8')

table = file.add_sheet('student')

txt = open('./student.txt').read()

json_txt = json.loads(txt)

for x in range(len(json_txt)):
    table.write(x, 0, x+1)
    for y in range(len(json_txt[str(x+1)])):
        table.write(x, y+1, json_txt[str(x+1)][y])

file.save('student.xls')
