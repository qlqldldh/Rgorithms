def input_init():
    str1 = "".join(["_", input()])
    str2 = "".join(["_", input()])
    return str1, str2


def join_str(sub_str1, sub_str2):
    return "".join([sub_str1, sub_str2]) if sub_str1 is not None else sub_str2


def longer_str(sub_str1, sub_str2):
    if sub_str1 is None or sub_str2 is None:
        return sub_str1 or sub_str2
    else:
        return sub_str1 if len(sub_str1) >= len(sub_str2) else sub_str2


def lcs(str1, str2):
    dp_row_size = len(str1)
    dp_col_size = len(str2)

    dp = [[None for _ in range(dp_col_size)] for _ in range(dp_row_size)]

    for i in range(1, dp_row_size):
        for j in range(1, dp_col_size):
            if str1[i] != str2[j]:
                dp[i][j] = longer_str(dp[i][j-1], dp[i-1][j])
            else:
                dp[i][j] = join_str(dp[i-1][j-1], str2[j])

    return dp[dp_row_size - 1][dp_col_size - 1]


def solution():
    input_str1, input_str2 = input_init()
    result = lcs(input_str1, input_str2)

    if result is None:
        print(0)
    else:
        print(len(result))
        print(result)


solution()