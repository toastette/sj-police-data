# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 13:19:27 2019

@author: Wendy
"""

import pandas as pd
old_year = 2004
new_year = 2019
for years in range(new_year - old_year + 1):
    files = "police_calls" + str(years) + ".csv"
    (str(years) + "_df") = pd.read_csv(files)