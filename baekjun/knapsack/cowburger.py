def set_init_data():
	return map(int, input().split())


def set_data(N, cheese, f_fries):
	for n in range(1, N + 1):
		cheese[n], f_fries[n] = map(int, input().split())


def fill_dp(N,M,K,cheese,f_fries):
	dp = [[[0 for _ in range(301)] for _ in range(301)] for _ in range(101)]

	for n in range(1, N + 1):
		for m in range(1, M + 1):
			for k in range(1, K + 1):
				if m >= cheese[n] and k >= f_fries[n]:
					dp[n][m][k] = max(dp[n-1][m][k], dp[n-1][m-cheese[n]][k-f_fries[n]] + 1)
				else:
					dp[n][m][k] = dp[n-1][m][k]
	return dp


def solution():
	N, M, K = set_init_data()
	cheese = [0 for _ in range(301)]
	f_fries = [0 for _ in range(301)]
	set_data(N, cheese, f_fries)
	dp = fill_dp(N,M,K,cheese, f_fries)
	return dp[N][M][K]


print(solution())

