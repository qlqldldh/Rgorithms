import sys

sys.setrecursionlimit(10 ** 7)


def dfs(location, _bamboos, _dp):
    row, col = location
    if _dp[row][col] != 0:
        return _dp[row][col]

    dp_values = [0]
    direcs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for direc in direcs:
        next_row, next_col = row + direc[0], col + direc[1]
        if not (0 <= next_row < len(_bamboos) and 0 <= next_col < len(_bamboos)):
            continue
        if _bamboos[row][col] > _bamboos[next_row][next_col]:
            dp_values.append(dfs((next_row, next_col), _bamboos, _dp))

    _dp[row][col] = max(dp_values) + 1
    return _dp[row][col]


def solution():
    answer = 0
    n = int(input())
    bamboos = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs((i, j), bamboos, dp))

    return answer


print(solution())
