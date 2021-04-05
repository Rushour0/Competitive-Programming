#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
d = {1:[[8,3,4],[1,5,9],[6,7,2]],2:[[4,9,2],[3,5,7],[8,1,6]],3:[[2,7,6],[9,5,1],[4,3,8]],0:[[6,1,8],[7,5,3],[2,9,4]]}
def formingMagicSquare(s):
    minboi = 1000
    global d
    for i in range(4):
        count = 0
        for a,b in zip(d[i],s):
            for x,y in zip(reversed(a),b):
                count+=abs(x-y)
        minboi = min(minboi,count)
        count = 0
        for a,b in zip(d[i],s):
            for x,y in zip(a,b):
                count+=abs(x-y)
        minboi = min(minboi,count)
        count = 0
        for a,b in zip(reversed(d[i]),s):
            for x,y in zip(reversed(a),b):
                count+=abs(x-y)
        minboi = min(minboi,count)
        count = 0
        for a,b in zip(reversed(d[i]),s):
            for x,y in zip(a,b):
                count+=abs(x-y)
        minboi = min(minboi,count)
    return minboi
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
