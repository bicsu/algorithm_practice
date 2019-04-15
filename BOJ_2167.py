# 누적합 / 부분합

ns = list(map(int, input().split()))

a = ns[0]
b = ns[1]
arr = []
for i in range(a) :
	inputs = list(map(int, input().split()))
	arr.append(inputs)

dp = [[0 for _ in range(b+1)] for _ in range(a+1) ]
for i in range(1,a+1):
	for j in range(1,b+1):
		dp[i][j]=dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]
times = int(input())
for it in range(times):
	haps = list(map(int, input().split()))

	a = haps[0]
	b = haps[1]
	c = haps[2]
	d = haps[3]

	print(dp[c][d]-dp[c][b-1]-dp[a-1][d]+dp[a-1][b-1])
