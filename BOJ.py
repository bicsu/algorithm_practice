#17173

n, m = map(int, input().split())
k_list = list(map(int, input().split()))
n_list = list(range(1,n+1))
dap = []
for i in k_list:
	for j in n_list:
		if i * j in n_list:
			dap.append(i*j)
dap = set(dap)
print(sum(list(dap)))