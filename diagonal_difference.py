#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    """
    This function receives a parameter arr, which is a square matrix, calculates the main and secondary diagonals and returns the absolute value of the difference between the diagonals
    :param arr: list - square matrix
    :return: int - the absolute value of the difference between the diagonals
    """
    n = len(arr)
    main_diagonal = secondary_diagonal = 0
    for i in range(n):
        #for the main diagonal i equal to j
        main_diagonal += arr[i][i]

    
    for i, j in zip(range(n), range(n-1, -1, -1)):
        secondary_diagonal += arr[i][j]

    """
    Another way
    for i, j in zip(range(n), range(n-1, -1, -1)):
        main_diagonal += arr[i][i]
        secondary_diagonal += arr[i][j]
    """

    return abs(main_diagonal - secondary_diagonal)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()