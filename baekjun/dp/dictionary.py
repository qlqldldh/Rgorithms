INF = 1000000001


def get_init_input():
    return map(int, input().split())


def set_dp_array(dp, n, m):
    for i in range(n + m + 1):
        dp[i][0] = 1
    for i in range(1, n + m + 1):
        for j in range(1, n + m + 1):
            if dp[i-1][j-1] + dp[i-1][j] >= INF:
                dp[i][j] = INF
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


def solution():
    answer = ""
    n, m, k = get_init_input()
    dp = [[0 for _ in range(201)] for _ in range(201)]
    set_dp_array(dp, n, m)

    if dp[n + m][n] < k:
        return -1

    rem_n, rem_m = n, m
    for i in range(n + m):
        if dp[rem_n + rem_m - 1][rem_m] < k:
            answer += "z"
            k -= dp[rem_n + rem_m - 1][rem_m]
            rem_m -= 1
        else:
            answer += "a"
            rem_n -= 1
        if rem_n == 0:
            while rem_m != 0:
                answer += "z"
                rem_m -= 1
            break
        if rem_m == 0:
            while rem_n != 0:
                answer += "a"
                rem_n -= 1
            break
    return answer


print(solution())
