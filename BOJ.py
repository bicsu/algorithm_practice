import sys	
try :
	rule = {}
	n = int(sys.stdin.readline())

	for i in range(1,11):
		rule[i] = []

	for i in range(1,11):
		for j in range(1,5):
			rule[i].append(i**j%10)
	rule[10] = [10,10,10,10]
	for i in range(n):
		a, b = map(int, sys.stdin.readline().split())
		if a%10 == 0 :
			print(rule[10][b%4-1])	
		else :
			print(rule[a%10][b%4-1])
except :
	exit()