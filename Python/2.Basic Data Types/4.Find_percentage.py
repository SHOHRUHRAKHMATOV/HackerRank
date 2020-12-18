# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
score = 0
Sum = 0
for key, value in student_marks.items():
    if query_name == key:
        score = value
Sum = sum(score)/len(score)
print("{:.2f}".format(Sum))