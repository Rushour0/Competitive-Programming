import collections
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    num = [i for i in range(1,n+1)]
    d = []
    count,total = 0,0
    for i,j in zip(l,num):
        d.append(i-j)
    occurences = collections.Counter(d)
    for i in occurences:
        if occurences[i]!=1:
            n = occurences[i]
            total += n*(n-1)//2
    print(total)