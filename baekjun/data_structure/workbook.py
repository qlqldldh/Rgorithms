def get_value_from_input():
    return map(int, input().split())


def sort_except_conds(_lst, _conds):
    for i in range(1, len(_lst) - 1):
        if _lst[i] > _lst[i + 1] and (_lst[i], _lst[i + 1]) not in _conds:
            _lst[i], _lst[i + 1] = _lst[i + 1], _lst[i]


n, m = get_value_from_input()

lst = [i for i in range(n + 1)]
conds = []

for _ in range(m):
    a, b = get_value_from_input()
    conds.append((a, b))
    if a < b or lst[a] < lst[b]:
        continue

    lst[a], lst[b] = lst[b], lst[a]

sort_except_conds(lst, conds)

for i in range(1, len(lst)):
    print(lst[i], end=" ")
