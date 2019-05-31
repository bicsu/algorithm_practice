a, b = map(int, input().split())


coins = []
for i in range(a):
	coins.append(int(input()))

coins.sort(reverse=True)
dap = 0
for i in coins:
	while b >= i:
		dap += b // i 
		b %= i
print(dap)

