n = int(input())

for i in range(n):
	inputs = input()
	l = 0
	hap = 0 
	total = 0
	while l < len(inputs):

		if inputs[l] == 'O':
			hap += 1
		else:
			hap = 0 
		l +=1
		total += hap
	print(total)