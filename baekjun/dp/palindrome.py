def get_single_value_from_input():
    return int(input())


def get_list_value_from_input():
    return list(map(int, input().split()))


def is_palindrome(_numbers, _dp, first, last):
    return _numbers[first] == _numbers[last] and _dp[first + 1][last - 1] == 1


def fill_dp_by_numbers(_dp, _numbers):
    for i in range(len(_numbers)):
        _dp[i][i] = 1

    for i in range(len(_numbers) - 1):
        if _numbers[i] == _numbers[i + 1]:
            _dp[i][i + 1] = 1

    for i in range(3, len(_numbers)):  # parsing length
        for j in range(len(_numbers)):  # current location of start point
            first, last = j, i + j - 1
            if last >= len(_numbers):
                break
            if is_palindrome(_numbers, _dp, first, last):
                _dp[first][last] = 1


def solution():
    answer = list()
    n = get_single_value_from_input()
    numbers = get_list_value_from_input()

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    fill_dp_by_numbers(dp, numbers)

    question_count = get_single_value_from_input()
    for _ in range(question_count):
        first, last = get_list_value_from_input()
        answer.append(dp[first - 1][last - 1])

    return answer


for ans in solution():
    print(ans)
