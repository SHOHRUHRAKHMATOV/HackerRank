# https://www.hackerrank.com/challenges/merge-the-tools/problem

import textwrap
def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))