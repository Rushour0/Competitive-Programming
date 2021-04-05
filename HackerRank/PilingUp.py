def chk(s,a):
    pre = a[0]
    for i in range(s-1):
        if pre>=a[i+1]:
            store = i
        else:
            return i
    return i
def chkr(s,a,j):
    pre = a[-1]
    for i in range(s-j-1):
        if pre<a[-i-1]:
            return print('No')
    return print('Yes')
for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    chkr(n,l,chk(n,l))