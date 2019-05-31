n = int(input())

times = list(map(int, input().split()))

def sums(arr):
	hap = 0
	res = []
	for i in arr:
		hap+=i
		res.append(hap)
	return sum(res)
times.sort()
print(sums(times))