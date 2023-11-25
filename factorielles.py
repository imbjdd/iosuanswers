inp = [1831,1298,1909,1785,2105,1916,1112,2378,1180,1901,2427,2178,2804,1241,2434,2475,2617,2324,1211,2587,2701,2109,2305,1765,1571,2385,1923,1498,1450,2291,2569,2591,1829,2766,1105,2982,2410,2447,2987,1056,1307,1379,1872,2422,2172,2328,2917,1123,1125,1887]
import sys
sys.set_int_max_str_digits(0)

def fact(N):
	res = 0
	fact = 1
	for i in range(1,N+1):
		fact *= i
		res += fact
	return res

f = open("out1.txt", "a")
for val in inp:
	f.write(str(fact(val)))
	f.write('\n')
f.close()
