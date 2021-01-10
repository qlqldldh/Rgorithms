N, M = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [0 for _ in range(1000001)]

for i in range(N):
	for j in range(sum(costs), costs[i]-1, -1):
		dp[j] = max(dp[j], dp[j-costs[i]]+memories[i])

for i in range(sum(costs)):
	if dp[i] >= M:
		print(i)
		break
