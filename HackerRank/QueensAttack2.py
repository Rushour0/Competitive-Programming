n,k = map(int,input().split())
py,px = map(int,input().split())
ur = n-max(px,py)
dl = min(px,py)-1
ul = min(n-py,px-1)
ulf = 1 if n-py>px-1 else 0
drf = 1 if py-1>n-px else 0
dr = min(py-1,n-px)
u = n-py
d = py-1
r = n-px
l = px-1
for i in range(k):
    yi,xi = map(int,input().split())
    xo,yo = xi - px,yi - py
    if xo>0 and yo>0:
        if xo == yo and ur>xo-1:
            ur = xo-1
    elif xo<0 and yo<0:
        if xo == yo and dl>0-xo-1:
            dl = 0-xo-1
    elif xo<0 and yo>0:
        if xo+yo==0:
            if ulf == 1:
                if ul>yo-1:
                    ul=yo-1
            else:
                if ul>0-xo-1:
                    ul = -1-xo
    elif xo>0 and yo<0:
        if xo+yo == 0:
            if drf == 1:
                if dr>-1-yo:
                    dr = -1-yo
            else:
                if dr>xo-1:
                    dr = xo-1
    elif xo==0:
        if yo>0:
            if u>yo-1:
                u = yo-1
        else:
            if d>-yo-1:
                d = -yo-1
    elif yo==0:
        if xo>0:
            if r>xo-1:
                r = xo-1
        else:
            if l>-xo-1:
                l = -xo-1
print(u+d+l+r+ul+dr+dl+ur)