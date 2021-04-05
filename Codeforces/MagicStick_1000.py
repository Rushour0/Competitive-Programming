for i in range(int(input())):
    a,b = map(int,input().split())
    if (a in [1,3] and b>a)or(a==2 and b>3):
        print('NO')
    else:
        print('YES')