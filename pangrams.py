#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvxwyz'
    if all(letter in s.lower() for letter in alphabet):
        return 'pangram'
    else:
        return 'not pangram'
    
    """
    Another Way
    alphabet = 'abcdefghijklmnopqrstuvxwyz'
    for letter in alphabet:
        if not letter in s.lower():
            return 'not pangram'
    # If the letter is not in s, it returns that s is not a pangram and no further iterations are necessary.    
    return 'pangram'
    """

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()