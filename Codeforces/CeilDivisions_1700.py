t =int(input())
def chk(n):
	g= n
	c= 0
	if n>12:
		while n!=0:
			n=int(n/12)
			c+=1
		print(g+c)
		for i in range(g-4):
			if i<9:
				print(i+3,g)
			else:
				print(i+4,g)
		for i in range(c):
			print(g,12)
		print(12 ,2)
		print(12 ,2)
		print(12 ,2)
		print(12 ,2)
	else:
		if n>8and n<13:
			print(n+1)
		elif n<9 and n>4:
			print(n)
		else:
			print(n-1)
		for i in range(n-3):
			print(i+3,n)
		while n!=1:
			print(g,2)
			n= n-int(n/2)
			c+=1
		
		
		
l =[]
for i in range(t):
	l.append(int(input()))
for i in l:
	chk(i)