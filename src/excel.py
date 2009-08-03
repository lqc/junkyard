# -*- coding: utf-8 -*-
import xlrd
import sys

book = xlrd.open_workbook(filename='test.xls')

l = []

for sheet in book.sheets():
    for i in xrange(0, sheet.nrows):
        row = sheet.row(i)
        for cell in row:            
            if cell.ctype == xlrd.XL_CELL_TEXT:
                l.append( cell.value.encode('cp1250') )
            else:
                l.append( str(cell.value) )

print '[' +', '.join(l) + ']'
print ''