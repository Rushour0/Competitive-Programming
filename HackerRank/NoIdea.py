n,m = map(int,input().split())
l = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ad,bd = {},{}
for i in range(m):
    ad[a[i]] = 1
    bd[b[i]] = 1
c=0   
for i in l:
    if i in ad:
        c+=1
    elif i in bd:
        c-=1
print(c)
