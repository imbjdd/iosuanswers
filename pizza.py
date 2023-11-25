
f = open("out_pizza.txt", "a")

with open("inp_pizza.txt", "r") as file:
    for l in file.readlines():
    	n = int(l)
    	f.write(str((n*n+n+2)//2)+'\n')


f.close()
