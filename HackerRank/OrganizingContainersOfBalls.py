c = []
for i in range(int(input())):
    n = int(input())
    r = []
    c = [0]*n
    
    for _ in range(n):
        l = list(map(int,input().split()))
        count = 0
        for j in range(n):
            c[j]+=l[j]    
            count+=l[j]
        r.append(count)
    c = sorted(c)
    r = sorted(r)
    if r!=c:
        print('Impossible')
    else:
        print('Possible')