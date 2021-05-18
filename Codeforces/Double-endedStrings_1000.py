def solve(s1,s2,n1,n2):
    for i in range(n1,-1,-1):
        for j in range(n1-i+1):
            if s1[j:j+i] in s2:
                return i
    return 1
for _ in range(int(input())):
    s1 = input()
    s2 = input()
    n1,n2 = len(s1),len(s2)
    count = solve(s1,s2,n1,n2)
    print(n1+n2-2*count)