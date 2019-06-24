#1406
import sys
try :
	s = list(sys.stdin.readline().rstrip())
	n = int(sys.stdin.readline())
	cursor = len(s)+1
	for i in range(n):
		cmd = sys.stdin.readline().rstrip()
		# print('first s:', s)
		# print('i:',i, 'first len:',len(s),'first cursor:',cursor)
		if len(cmd)== 1:
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
					# print('B states',cursor, len(s))
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
		# print('cmd?',cmd)
		# print('s:', s)
		# print('len:',len(s),'cursor:',cursor)


	print(''.join(s), end='\n')
except :
	exit()
