# https://www.hackerrank.com/challenges/string-validators/submissions/code/188154356

if __name__ == '__main__':
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))