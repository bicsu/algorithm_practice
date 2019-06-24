n, m = map(int, input().split())


mok = n // m 
dap = n

if mok >= m :
	dap += mok
	while mok >= m :
		mok = mok // m 
		dap += mok
else :
	dap += mok

print(dap)