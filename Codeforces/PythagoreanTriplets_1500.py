def chkr():
    n = int(input())
    m = 4
    c = 0
    while n>m:
        c+=1
        m = 2*(c+1)*(c+2)
    print(c)
for _ in range(int(input())):
    chkr()
