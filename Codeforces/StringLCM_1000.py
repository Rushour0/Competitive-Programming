def strs():
    return list(map(str,input().split()))
def lcm0(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm
for i in range(int(input())):
    l = input()
    c = input()
    ll = len(l)
    lc = len(c)
    if ll%lc ==0 and int(ll/lc)*c==l:
        print(l)
    elif int(lcm0(ll,lc)/ll)*l == int(lcm0(ll,lc)/lc)*c:
        print(int(lcm0(ll,lc)/ll)*l)
    else:
        print(-1)