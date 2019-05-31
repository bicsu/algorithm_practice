#1406
try :
	s = list(input())
	n = int(input())
	cursor = len(s)+1
	for i in range(n):
		cmd = input()
		if len(cmd) == 1:
			if cmd == 'L':
				if cursor == 0 :
					continue
				else :
					cursor -= 1
			elif cmd == 'D':
				if cursor == len(s)+1 :
					continue
				else :
					cursor += 1

			elif cmd == 'B':
				if cursor == 0:
					pass
				else :
					if cursor-2 < 0 :
						cursor = 1
					else :
						del s[cursor-2]
						cursor -= 1

		else :
			p, new_s = cmd.split()
			s = list(s)
			if cursor == 0 :
				s.insert(0, new_s)
			else : 
				s.insert(cursor-1, new_s)
			cursor += 1
	print(''.join(s), end='\n')
except:
	exit()