n,k = map(int,input().split())
l = list(map(int,input().split()))
temp,remember = float('INF'),0
val = sum(l[:k])
for i in range(n-k+1):
    if val<temp:
        temp = val
        remember = i+1
    try:
        val = val-l[i]+l[i+k]
    except:
        break
print(remember) 