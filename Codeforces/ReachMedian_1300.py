n,s = map(int,input().split())
l = sorted(list(map(int,input().split())))
cost=0
boi0 = l[:n//2]
boi1 = l[n//2+1:]
for i in range(n//2):
    if boi0[-1-i]>s:
        cost+=abs(boi0[-1-i]-s)
        boi0[-1-i] = s
    if boi1[i]<s:
        cost+=abs(boi1[i]-s)
        boi1[i] = s
cost+=abs(l[n//2]-s)
print(cost)