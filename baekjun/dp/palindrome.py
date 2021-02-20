def get_single_value_from_input():
    return int(input())


def get_list_value_from_input():
    return list(map(int, input().split()))


def is_palindrome(_numbers, first, last):
    return all(_numbers[i] == _numbers[last + first - i] for i in range(first, (first + last) // 2 + 1))


def fill_dp_by_numbers(_dp, _numbers):
    for i in range(1, len(_numbers)):  # parsing length
        for j in range(len(_numbers)):  # current location of start point
            if i == 1:
                _dp[j][j] = 1
                break
            first, last = j, i + j - 1
            if last >= len(_numbers) or not is_palindrome(_numbers, first, last):
                break
            _dp[first][last] = 1


def solution():
    answer = list()
    n = get_single_value_from_input()
    numbers = get_list_value_from_input()

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    fill_dp_by_numbers(dp, numbers)

    print(dp)

    question_count = get_single_value_from_input()
    for seq in range(question_count):
        first, last = get_list_value_from_input()
        answer.append(dp[first - 1][last - 1])

    return answer


for ans in solution():
    print(ans)
