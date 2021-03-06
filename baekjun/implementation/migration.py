BOUNDARY = -1


def get_nations_info():
    n, m, k = map(int, input().split())

    nations = [[-1 for _ in range(n + 2)] for _ in range(n + 2)]

    for i in range(1, n + 1):
        lst = list(map(int, input().split()))
        nations[i][1 : n + 1] = lst

    return nations, m, k


def get_marking_map(n):
    return [[False for _ in range(n + 2)] for _ in range(n + 2)]


def is_diff_in_range(nation1, nation2, min_value, max_value):  # need to rename
    return min_value <= abs(nation1 - nation2) <= max_value


def is_boundary(people_num):
    return people_num == BOUNDARY


def get_union_total(nations, union):
    total = 0
    for loc in union:
        total += nations[loc[0]][loc[1]]

    return total


def set_union_to_average(nations, union):
    total = get_union_total(nations, union)
    average = total // len(union)

    while union:
        loc = union.pop()
        nations[loc[0]][loc[1]] = average


def dfs(nations, marking_map, loc, union, min_value, max_value):
    direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for d in direc:
        row, col = loc[0] + d[0], loc[1] + d[1]
        target_nation = nations[row][col]
        if (
            is_boundary(target_nation)
            or marking_map[row][col]
            or not is_diff_in_range(
                nations[loc[0]][loc[1]], target_nation, min_value, max_value
            )
        ):
            continue

        marking_map[row][col] = True
        union.append((row, col))
        dfs(nations, marking_map, (row, col), union, min_value, max_value)


def migrate(nations, min_value, max_value):
    answer = -1
    direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    union = list()
    flag = True

    while flag:
        answer += 1
        flag = False
        marking_map = get_marking_map(len(nations) - 2)

        for i in range(1, len(nations) - 1):
            for j in range(1, len(nations) - 1):
                if marking_map[i][j]:
                    continue

                for d in direc:
                    row, col = i + d[0], j + d[1]
                    target_nation = nations[row][col]
                    if (
                        is_boundary(target_nation)
                        or not is_diff_in_range(
                            nations[i][j], target_nation, min_value, max_value
                        )
                        or marking_map[row][col]
                    ):
                        continue
                    flag = True
                    union.append((i, j))
                    marking_map[i][j] = True
                    dfs(nations, marking_map, (i, j), union, min_value, max_value)
                    set_union_to_average(nations, union)
    return answer


def solution():
    nations, min_value, max_value = get_nations_info()

    return migrate(nations, min_value, max_value)


print(solution())
