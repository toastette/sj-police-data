# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:29:19 2019

@author: Wendy
"""
import csv

year = 2004
newest_year = 2019
for files in range (newest_year - year + 1):
    with open("policecalls" + str(year) + ".csv") as read:
        reader = csv.reader(read)
        next(reader)
        with open("policecalls" + str(year) + "_fixed.csv", "w", newline = '') as write_to:
            writer = csv.writer(write_to)
            for row in reader:
                writer.writerow(row)
    year += 1