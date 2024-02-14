"""
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] = t[i]:
            res = '0';
        else:
            res = '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
"""
# Above is the code to be 'fixed'
# Can modify at most three lines in the given code and you cannot add or remove lines to the code.
# Analyzing the code, lines 5, 6 and 8 must be modified, as they contain syntax errors, so these lines are the ones to be modified.
# 
# Solution

def strings_xor(s, t):
    """
    This funcion takes a paramenters two strings symbolizing a 'set of bits', applies the XOR operation to each item in both strings and returns the resulting 'set of bits'.
    :param s: str - 'set of bits'
    :param t: str - 'set of bits'
    :return: str - the resulting 'set of bits'
    """
    
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]: # fixed equality for comparison
            res += '0' # Concatenating bits in the string, otherwise 'res' would only have 1 element
        else:
            res += '1' # Concatenating bits in the string, otherwise 'res' would only have 1 element

    return res

s = input()
t = input()
print(strings_xor(s, t))