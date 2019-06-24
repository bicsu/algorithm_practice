#1253

n = int(input())

nlist = list(map(int, input().split()))
nlist.sort()
dap = 0
done = False
for i, num in enumerate(nlist):
	for j, num2 in enumerate(nlist[2:i]):
		if num == num2 + nlist[j-1]:
			print(num)
			dap += 1

print(dap)