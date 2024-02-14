#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def permuting(A, B, k):
    """
    This function takes as a parameter 2 arrays of integers and 1 integer k and permutes the arrays so that A[i] + B[i] >= k (item i of A plus item i of B is greater than or equal to k) is satisfied.
    :param A: list - list of integer
    :param B: list - list of integer
    :param k: int - integer to be used for comparison
    Parameters in python are passed by reference, so any local change to a parameter will affect it globally, so function do not return value.
    """

    backup = 0
    A.sort() # This will make it easier to compare with matrix B

    for index_a, a in enumerate(A):
        for index_b in range(index_a, len(B)):  # traverses array B, disregarding the items in the correct position
            if a + B[index_b] >= k:
                backup = B[index_a]
                B[index_a] = B[index_b]
                B[index_b] = backup
                break


def twoArrays(k, A, B):
    """
    This function takes as a parameter 2 arrays of integers and 1 integer k and permutes the arrays so that A[i] + B[i] >= k (item i of A plus item i of B is greater than or equal to k) is satisfied.
    :param A: list - list of integer
    :param B: list - list of integer
    :param k: int - integer to be used for comparison
    :return: str - returns 'YES' if all elements of A and B satisfy the condition A[i] + B[i] >= k, 'NO' otherwise.
    """

    permuting(A, B, k)
    if all(a + b >= k for a, b in zip(A, B)):
        return 'YES'
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()