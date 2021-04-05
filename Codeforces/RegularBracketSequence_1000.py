for i in range(int(input())):
    l = input()
    print('NO' if l.endswith('(') or l.startswith(')') or len(l)%2==1 else "YES")