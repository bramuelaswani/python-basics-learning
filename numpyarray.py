# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:31:59 2021

@author: User
"""

import numpy as np
np_heights = np.array([[1.75,1.65,1.8,1.5],[1.56,1.70,1.4,1.29],[1.49,1.68,1.3,1.8]])
np.sort(np_heights[0])
print(np.mean(np_heights[:,0]))