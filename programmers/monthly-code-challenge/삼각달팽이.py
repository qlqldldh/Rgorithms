def solution(n):
    answer = []

    for i in range(1, n + 1):
        lst = [0 for j in range(i)]
        answer.append(lst)
    answer[n - 1].append(-1)
    answer.append([-1 for k in range(n)])  # row-padding

    direc = [[1, 0], [0, 1], [-1, -1]]
    sw = int(0)
    lim = int((n * (n + 1)) / 2)

    r, c = 0, 0

    for cnt in range(1, lim + 1):
        answer[r][c] = cnt

        if answer[r + direc[sw][0]][c + direc[sw][1]] != 0:
            sw = (sw + 1) % 3

        r += direc[sw][0]
        c += direc[sw][1]

    result = []

    for i in range(n):
        for j in range(len(answer[i])):
            result.append(answer[i][j])

    result.pop()
    return result
