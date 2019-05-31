try :
	n = int(input())
	height = 0
	temp_height = 0
	h_list = [0, 0]
	n_list = list(map(int, input().split()))
	for i, j in zip(n_list, n_list[1:]) :
		
		if j > i :
			height += j-i

		else :
			if temp_height < height :
				temp_height = height
			
			height = 0
		print('temp:',temp_height,'h:',height)


	print(max(temp_height, height))
except : 
	exit()