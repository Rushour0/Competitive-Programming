for i in range(int(input())):
    r = int(input())
    rl = list(map(int,input().split()))
    b = int(input())
    bl = list(map(int,input().split()))
    maxr,maxb = 0,0
    r0,b0 = 0,0
    for j in rl:
        r0+=j
        if r0>maxr:
            maxr = r0
    for j in bl:
        b0+=j
        if b0>maxb:
            maxb = b0
    print(maxb+maxr)