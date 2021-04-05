cubes = {}
def solve():
    val = int(input())
    for i in cubes:
        if val-i and val-i in cubes:
            print("Yes")
            return
        elif val-i<0:
            print("No")
            return
    return print("No")
for i in range(1,10001):
    cubes[i**3] = 0
for i in range(int(input())):
    solve()