#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import xlwt
import json

File = xlwt.Workbook(encoding = 'utf-8')

table = File.add_sheet('city')

txt = open('./city.txt').read()

json_txt = json.loads(txt)

print json_txt

for x in range(len(json_txt)):
    table.write(x, 0, json_txt.keys()[x])
    for y in range(len(json_txt[str(x+1)])-1):
        table.write(x, y+1, json_txt[str(x+1)])

File.save('city.xls')
