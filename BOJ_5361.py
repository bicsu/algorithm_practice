a = 350.34
b = 230.90
c = 190.55
d = 125.30
e = 180.90

brr = [a,b,c,d,e]


n = int(input())
arr = []

for i in range(n):
	dap = 0
	needs = list(map(int, input().split()))
	for j in range(5):
		dap += needs[j] * brr[j]
	print('$%.2f'%(dap))
