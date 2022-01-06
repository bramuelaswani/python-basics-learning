# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 19:14:34 2021

@author: User
"""

import numpy as np
alist=[2,4,5,4]
list_np=np.array(alist)
blist=[3,5,6,5]
blist_np=np.array(blist)
total=list_np+blist_np
print(total)
print(list_np**2)
print(total>5)
print([[total>5]])