def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        lst=[]
        for j in range(k):
            if string[i+j] not in lst:
                lst.append(string[i+j])
        print(''.join(lst))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)