INF_VALUE = 1000000001


def dfs(l_idx, r_idx, _cost, _sum_cost, _dp):
    if _dp[l_idx][r_idx] != INF_VALUE:
        return _dp[l_idx][r_idx]

    if l_idx == r_idx:
        _dp[l_idx][r_idx] = 0
        return _dp[l_idx][r_idx]

    if r_idx - l_idx == 1:
        _dp[l_idx][r_idx] = _cost[l_idx] + _cost[r_idx]
        return _dp[l_idx][r_idx]

    for x in range(l_idx, r_idx):
        _dp[l_idx][r_idx] = min(
            _dp[l_idx][r_idx],
            dfs(l_idx, x, _cost, _sum_cost, _dp)
            + dfs(x + 1, r_idx, _cost, _sum_cost, _dp),
        )

    _dp[l_idx][r_idx] += _sum_cost[r_idx] - _sum_cost[l_idx - 1]
    return _dp[l_idx][r_idx]


def get_input():
    return int(input())


def get_costs():
    _costs = list(map(int, input().split()))
    _costs.insert(0, 0)
    return _costs


def get_sum_of_costs(_cost, _k):
    _sum_cost = [0 for _ in range(_k + 1)]
    for i in range(1, len(_cost)):
        _sum_cost[i] = _sum_cost[i - 1] + _cost[i]

    return _sum_cost


def solution():
    t = get_input()

    for _ in range(t):
        k = get_input()
        cost = get_costs()
        sum_cost = get_sum_of_costs(cost, k)

        dp = [[INF_VALUE for _ in range(k + 1)] for _ in range(k + 1)]
        return dfs(1, k, cost, sum_cost, dp)


print(solution())
