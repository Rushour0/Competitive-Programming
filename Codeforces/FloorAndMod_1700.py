for __ in range(int(input())):
    a,b = map(int,input().split())
    c = 0
    n = 1
    while n**2<a:
        c+=max(0,min(b,a//n-1)-n)
        n+=1
    print(c)