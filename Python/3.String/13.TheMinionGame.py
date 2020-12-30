# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = 'AEIOU'
    count1 = 0
    count2 = 0
    for i in range(len(string)):
        if string[i] in vowels:
            count1 += (len(s)-i)
        else:
            count2 += (len(s)-i)
    if count1 > count2:
        print('Kevin', count1)
    elif(count1 < count2):
        print('Stuart', count2)
    else:
        print('Draw')
