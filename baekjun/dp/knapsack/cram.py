def set_init_data():
	return map(int, input().split())


def set_data(N, study_time, chapter_score):
	for n in range(1, N + 1):
		study_time[n], chapter_score[n] = map(int, input().split())


def fill_dp(N, T, study_time, chapter_score):
	dp = [[0 for _ in range(10001)] for _ in range(101)]
	
	for n in range(1, N + 1):
		for t in range(1, T + 1):
			if t >= study_time[n]:
				dp[n][t] = max(dp[n-1][t], dp[n-1][t-study_time[n]] + chapter_score[n])
			else:
				dp[n][t] = dp[n-1][t]
	return dp


def solution():
	N, T = set_init_data()
	
	study_time = [0 for _ in range(101)]
	chapter_score = [0 for _ in range(101)]
	set_data(N, study_time, chapter_score)
	
	dp = fill_dp(N, T, study_time, chapter_score)

	return dp[N][T]


print(solution())

