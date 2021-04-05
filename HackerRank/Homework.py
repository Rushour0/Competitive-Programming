t = int(input())
l = list(map(int,input().split()))
lr = l[:]
c = 0
pos = {}
por = {}
for i in l:
    pos[i] = c
    por[i] = c
    c+=1
s = sorted(l)
c,d = 0,0
for i in range(t):
    if l[i]!=s[i]:
        l[por[s[i]]] = l[i]
        por[l[i]] = por[s[i]]
        l[i] = s[i]
        por[s[i]] = i
        c+=1 
    if lr[i]!=s[-i-1]:
        lr[pos[s[-i-1]]] = lr[i]
        pos[lr[i]] = pos[s[-i-1]]
        lr[i] = s[-i-1]
        pos[s[-i-1]] = i
        d+=1
print(min(c,d))
