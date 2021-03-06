def scale(dp, sinker, n, now, left, right, possible):
    new = abs(left - right)
    if new not in possible:
        possible.append(new)
    if now == n:
        return 0
    if dp[now][new] == 0:
        # on left
        scale(dp, sinker, n, now + 1, left + sinker[now], right, possible)
        # on right
        scale(dp, sinker, n, now + 1, left, right + sinker[now], possible)
        # none
        scale(dp, sinker, n, now + 1, left, right, possible)

        dp[now][new] = 1


def solution():
    n = int(input())
    sinker = list(map(int, input().split()))
    m = int(input())
    bizs = list(map(int, input().split()))
    possible = []
    dp = [[0] * 15001 for i in range(n + 1)]

    scale(dp, sinker, n, 0, 0, 0, possible)

    for i in range(0, len(bizs)):
        if bizs[i] in possible:
            print("Y", end=" ")
        else:
            print("N", end=" ")


solution()
