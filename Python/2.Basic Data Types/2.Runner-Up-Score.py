# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

n = int(input())
arr = map(int, input().split())
arr = list(arr)
max_item = max(arr)
while max(arr) == max_item:
    arr.remove(max(arr))
print(max(arr))