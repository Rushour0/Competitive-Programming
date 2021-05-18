for _ in range(int(input())):
    n = int(input())
    if n!=2:
        lim = n*n
        odd,even = 1,2
        for i in range(n):
            for j in range(n):
                if odd<=lim:
                    print(odd,end = " ")
                    odd+=2
                else:
                    print(even,end = " ")
                    even+=2
            print()
    else:
        print(-1)