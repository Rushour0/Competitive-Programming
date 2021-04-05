#!/bin/python3

import math
import os
import random
import re
import sys
d = {0:'',1:' one',2:' two',3:' three',4:' four',5:' five',6:' six',7:' seven',8:' eight',9:' nine',10:' ten',11:' eleven',12:' twelve',13:' thirteen',14:' fourteen',15:' fifteen',16:' sixteen',17:' seventeen',18:' eighteen',19:' nineteen',20:'twenty'}

# Complete the timeInWords function below.
def timeInWords(h, m):
    if m>=30:
        h = h%12+1
        m = 60-m
        if m == 15:
            return f"quarter to{d[h]}"
        elif m == 30:
            return f"half past{d[h-1]}"
        elif m>19:
            return f"{d[20]}{d[(m)%10]} minutes to{d[h]}"      
        elif m == 1:
            return f"one minute to{d[h]}"
        elif m<20:
            return f"{d[m]} minutes to{d[h]}".lstrip()
    elif m == 0:
        return f"{d[h]} o' clock".lstrip()
    else:
        if m == 15:
            return f"quarter past{d[h]}"
        elif m>19:
            return f"{d[20]}{d[(m)%10]} minutes past{d[h]}"       
        elif m == 1:
            return f"one minute past{d[h]}"     
        elif m<20:
            return f"{d[m]} minutes past{d[h]}".lstrip()
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
