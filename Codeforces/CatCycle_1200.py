for _ in range(int(input())):
    n,k = map(int,input().split())
    x = int(n//2)+1
    if n%2 == 0:
        pri = n
        if k%n != 0:
            pri = k%n
        print(pri)
    else:
        ad = (k-1)//(x-1)
        k+=ad
        if k>n:
            k%=n
            if k%n == 0:
                k = n
        print(k)