n = int(input())

attend = {}
for i in range(n):
	log = input().split()
	if log[0] not in attend:
		attend[log[0]] = log[1]
	else : 
		del attend[log[0]]

poors = []
for i in attend:
	if attend[i] == "enter":
		poors.append(i)

poors.sort(reverse=True)
for i in poors:
	print(i)