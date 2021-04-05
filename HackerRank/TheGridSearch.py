def chk(r1,c1,t,q,x,y):
    for i in range(r1):
        if q[i]!=t[x+i][y:y+c1]:
            return 0
    return 1
def chkr():
    l= []
    ch = []
    r,c = map(int,input().split())
    for __ in range(r):
        l.append(input())
    r0,c0 = map(int,input().split())
    for __ in range(r0):
        ch.append(input())
    for i in range(r-r0+1):
        for j in range(c-c0+1):
            if chk(r0,c0,l,ch,i,j)==1:
                return print("YES")
    return print("NO")
for _ in range(int(input())):
    chkr()
