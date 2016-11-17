# -*- coding: utf-8 -*-
import csv
import json


if __name__ == '__main__':
    with open('l_result.json', 'r') as f:
        l = f.read()
    with open('c_result.json', 'r') as f:
        c = f.read()
    csvfile = file('csv.csv', 'w')
    writer = csv.writer(csvfile)
    writer.writerow(['p','l','c'])
    data = list()
    l = json.loads(l)
    c = json.loads(c)
    for p in l:
        data.append(('%.3f' % float(p), l[p], c[p]))
    writer.writerows(data)
    csvfile.close()
