# Problem: https://www.hackerrank.com/challenges/nested-list/problem

grades = {}
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score in grades.keys():
        grades[score].append(name)
    else:
        grades[score] = [name]

for _ in sorted(grades[sorted(grades)[1]]):
    print(_)
