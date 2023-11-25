import numpy as np

f = open("outsnail.txt", "a")

def snail_tail(M):
    res = []
    for i in range(len(M)-1, -1, -1):
        res.append(M[i][0])
    for i in range(1, len(M)):
        res.append(M[0][i])
    for i in range(1, len(M)):
        res.append(M[i][len(M)-1])
    for i in range(len(M)-2, 0,-1):
        res.append(M[len(M)-1][i])
    return res

def snail(inp):
    for t in range(0,1+len(inp)//2):
        f.write(' '.join(map(str, snail_tail(inp))))
        f.write(' ')
        inp = inp[1:-1, 1:-1]

mat =[]

with open("inp_snail.txt", "r") as file:
    for l in file.readlines():
        if len(l)==1:
            print(np.array(mat))
            snail(np.array(mat))
            f.write('\n')
            mat = []
        else:
            mat.append([int(c) for c in l.split(' ')])

f.close()
