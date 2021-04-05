def minion_game(s):
    v,c = 0,0
    n = len(s)
    for i in range(n):
        if s[i] in 'AEIOU':
            v+=n-i
        else:
            c+=n-i
    if c>v:
        print('Stuart',c)
    elif v>c:
        print('Kevin',v)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)