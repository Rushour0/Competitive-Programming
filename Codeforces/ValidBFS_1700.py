n = int(input())
pc = []
for i in range(n+1):
    pc.append(set())
for i in range(n-1):
    p,c = map(int,input().split())
    pc[p].add(c)
    pc[c].add(p)
l = list(map(int,input().split()))
front,back = 1,1
for i in l:
    #print(pc[i])
    front = back
    back += len(pc[i])
    if i!=1:
        back-=1        
    if front>=n:
        break
    for j in l[front:back]:
        #print(l[front:back])
        if j not in pc[i]:
            print("No")
            exit()
print("Yes")