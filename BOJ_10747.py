s = (input())
t = (input())
idx = s.index
boo = True
while boo == True:
	if t in s:
		for i in t:
			s = list(s)
			print((i))
			del s[idx(i)]
		s = ''.join(s)
	else :
		boo = False

print(''.join(s))