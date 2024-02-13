#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    negative = positive = zero = 0

    for number in arr:
        if number < 0:
            negative += 1
        elif number > 0:
            positive += 1
        else:
            zero += 1

    print(f"{positive / len(arr):.6f}\n{negative / len(arr):.6f}\n{zero / len(arr):.6f}")


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)