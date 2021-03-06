def solution():
    init_s = input()
    exp_s = input()

    answer = []

    for s in init_s:
        answer.append(s)
        if s == exp_s[-1] and ''.join(answer[-len(exp_s):]) == exp_s:
            del answer[-len(exp_s):]

    if not answer:
        print("FRULA")
    else:
        print("".join(answer))


solution()
