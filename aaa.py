#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    b = sum(set(a))
    ab = sum(a)
    ress = (2*b) - ab
    return ress
            

arr = [1,3,4,5,7,3,4,1,7]
l=lonelyinteger(arr)
print(l)
