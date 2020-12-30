# https://www.hackerrank.com/challenges/capitalize/problem

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s