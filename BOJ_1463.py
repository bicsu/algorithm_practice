x = int(input(""))
dap = list(range(x+1))
dap[0] = 0
dap[1] = 0
for i in range(2, x+1):
	dap[i] = dap[i-1] + 1
	if i % 3 == 0:
		dap[i] = min(dap[i//3]+1, dap[i])

	elif i % 2 == 0 :
		dap[i] = min(dap[i//2]+1, dap[i])
	print('i:',i,'dap',dap)
