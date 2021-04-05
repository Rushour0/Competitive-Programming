s = input()
n = len(s)
root = n**(1/2)
if root-int(root)!= float(0):
    l = int(root)
    u = l+1
    if l*u<n:
        l = u
else:
    l,u = int(root),int(root)
g = 0
main = ''
for i in range(u):
    v = ''
    for j in range(int(n/u)+1):
        try:
            v+=s[i+j*u]
        except:
            g+=1
    if i!=u-1:
        main+=v+' '
    else:
        main+=v
print(main)      
        
