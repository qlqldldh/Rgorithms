def solution():
    init_s = input()
    exp_s = input()

    last_char = exp_s[-1]
    stack = []
    length = len(exp_s)

    for char in init_s:
        stack.append(char)
        if char == last_char and ''.join(stack[-length:]) == exp_s:
            del stack[-length:]

    answer = ''.join(stack)

    if answer == '':
        print("FRULA")
    else:
        print(answer)


solution()
