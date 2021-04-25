def solution(s):
    mid_idx = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid_idx-1:mid_idx+1]

    return s[mid_idx]


if __name__ == "__main__":
    s = input("text: ")

    answer = solution(s)

    print(answer)

