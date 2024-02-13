#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    print(f'{sum(arr[:4])} {sum(arr[1:])}')

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)



"""
from functools import reduce
from operator import add

def maxmin(arr):
    arr.sort()

    print(f'{reduce(add, arr[:4]), 1}  {reduce(add, arr[1:], 1)}')"""


"""
def maxmin(arr):
    arr.sort()
    max = min = 0
    for index, number in enumerate(arr):
        if index < 4:
            min += number
        if index > 0:
            max += number
    print(f"{min}  {max}")

"""