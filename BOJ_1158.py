try : 
	arr = list(map(int, input().split()))
	n = arr[0]
	k = arr[1]
	ns = list(range(1,n+1))
	dap = []
	cursor = 0
	#k = k-1

	while ns !=[]:
	    if cursor + (k-1) <= len(ns)-1:
	        cursor += (k-1)
	        dap.append(ns.pop(cursor))
	    elif len(ns) == 1:
	        dap.append(ns.pop())
	    else : 
	        if cursor+k-1 >= len(ns)*2:
	            cursor -= len(ns)*(((cursor+k-1)//len(ns))-1)
	        cursor = cursor + k-1 - len(ns)
	        dap.append(ns.pop(cursor))
	st = '<'
	for i in dap:
		if i == dap[-1]:
			st = st+(str(i))
		else : 
			st = st+(str(i)+', ')

	print(st+'>')
except :
	exit()