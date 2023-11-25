import math

f = open("out_cube.txt", "a")

with open("inp_cube.txt", "r") as file:
    for l in file.readlines():
        inp = l.split(',') #dim, taille
        dime = int(inp[0])
        taillent = int(inp[1])
        nb_carre = sum([pow(i, dime) for i in range(taillent+1)])
        nb_rectangle = pow(taillent*(taillent+1)//2, dime) -nb_carre
        f.write(str(nb_carre)+' '+str(nb_rectangle))
        f.write('\n')

f.close()
