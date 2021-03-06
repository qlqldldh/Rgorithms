def get_single_value_from_input():
    return int(input())


def get_value_from_dp(_dp, _len, m):
    if _dp[_len] >= 0:
        return _dp[_len]

    _dp[_len] = 0

    for i in range(2, _len + 1, 2):
        _dp[_len] += get_value_from_dp(_dp, i - 2, m) * get_value_from_dp(
            _dp, _len - i, m
        )
        _dp[_len] %= m

    return _dp[_len]


def solution():
    dp = [-1 for _ in range(5001)]
    _mod = 1000000007
    t = get_single_value_from_input()
    for _ in range(t):
        length = get_single_value_from_input()
        if length % 2 == 1:
            print(0)
        else:
            print(get_value_from_dp(dp, length, _mod))


solution()
