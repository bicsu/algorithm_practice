t = int(input())
import sys
for i in range(t):
	n = int(sys.stdin.readline().rstrip())
	grades = []
	cnt = 0 
	for j in range(n):
		jum = list(map(int, sys.stdin.readline().rstrip().split()))
		grades.append(jum)
		grades=sorted(grades, key=lambda x : x[0])
	print(grades)