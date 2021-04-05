for __ in range(int(input())):
    a,b = map(int,input().split())
    c = []
    m,n = a,b
    count = 0
    if n == 1:
        n = 2
        count = 1
    for _ in range(30):
        co = count+_
        a,b = m,n+_
        while a>0:
            a//=b
            co+=1
        c.append(co)
    print(min(c))