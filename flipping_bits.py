#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def multiplication(a, b):
    return a * b

def flippingBits(n):
    number_binary = []
    binary_base = []
    for i in range(32):
        binary_base.insert(0, 2 ** i)

    if n == 0:
        number_binary.insert(0, 0) 
    else:
        while n > 0:
            number_binary.insert(0, n%2)
            n = n // 2
    for i in range(len(number_binary), 32):
        number_binary.insert(0, 0)

    for index, bit in enumerate(number_binary):
        if bit == 0:
            number_binary[index] = 1
        else:
            number_binary[index] = 0

    
    return sum(list(map(multiplication, number_binary, binary_base)))
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()