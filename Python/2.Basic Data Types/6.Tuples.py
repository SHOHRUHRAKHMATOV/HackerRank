#Problem: https://www.hackerrank.com/challenges/python-tuples/submissions/code/187767508
n = int(input())
ints = input().split()
t = tuple(int(i) for i in ints)
print(hash(t))