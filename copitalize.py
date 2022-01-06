# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:43:54 2021

@author: User
"""

s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)