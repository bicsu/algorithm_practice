#2751
try:
	n = int(input())
	nlist = []
	for i in range(n):
		nlist.append(int(ipnut()))
	nlist.sort()

	for i in nlist:
		print(i)
except:
	exit()