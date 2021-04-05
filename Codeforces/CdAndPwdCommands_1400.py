update = ['']
for __ in range(int(input())):
    l = input().split()
    if len(l) == 1:
         print('/')if len(update)==1 else print('/'.join(update)+'/')
    else:
        b=l[1].split('/')
        if(b[0]==''):
            update=['']
        for i in b:
            if i == '..' and len(update)>1:
                update.pop()
            elif i=='':
                continue
            else:
                update.append(i)