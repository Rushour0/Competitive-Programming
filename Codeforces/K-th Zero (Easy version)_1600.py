def query(e):
    print("?",1,e,flush = True)
    return e-int(input())

def solve():
    n,t = map(int,input().split())
    k = int(input())
    s,e = 1,n
    while True:
        mid = (s+e)//2
        t = query(mid)
        if t == k and s == e:
            return print("!",s)
        if t>=k:
            e = mid
        else:
            s = mid+1
    print("!",s)
solve()