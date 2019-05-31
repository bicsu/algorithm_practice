a, b = map(int, input().split())
dap = []
b = str(b)
cnt = 0 
for i in range(1, a+1):
	num = str(i)
	for j in num:
		if j == b:
			cnt +=1

print(cnt)
