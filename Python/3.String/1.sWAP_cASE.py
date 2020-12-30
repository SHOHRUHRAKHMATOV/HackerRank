# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    result = ''
    for i in s:
        if i == i.upper():
            result += i.lower()
        else:
            result += i.upper()
    return result
