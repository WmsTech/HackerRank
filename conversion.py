#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    h1 = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
    h2 = ['13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
    if s[:2] != '12':
        if s[-2:] == 'AM':
            return s[:-2]
        return h2[h1.index(s[:2])] + s[2:-2]
    else:
        if s[-2:] == 'PM':
            return s[:-2]
        return '00' + s[2:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

