#  Programmers - 2018 Kakao Blind Recruitment - Dart Game


def alpha_interpreter(ch):
    if ch == "S":
        return 1
    elif ch == "D":
        return 2
    elif ch == "T":
        return 3


def is_ten(i, dartResult):
    if dartResult[i] == str(1) and dartResult[i + 1] == str(0):
        return True
    return False


def spreading_value(ch, lst):
    if ch == "*":
        lst[-1] = lst[-1] * 2
        if len(lst) > 1:
            lst[-2] = lst[-2] * 2
    elif ch == "#":
        lst[-1] = -lst[-1]


def solution(dartResult):
    answer = 0

    flag = True
    rst_list = []
    for i in range(len(dartResult)):
        if flag:
            if dartResult[i].isdecimal():
                if is_ten(i, dartResult):
                    rst_list.append(10)
                    flag = False
                else:
                    rst_list.append(int(dartResult[i]))
            elif dartResult[i].isalpha():
                rst_list[-1] = pow(rst_list[-1], alpha_interpreter(dartResult[i]))
            else:
                spreading_value(dartResult[i], rst_list)
        else:
            flag = True
            pass
    for n in rst_list:
        answer += int(n)

    print(rst_list)

    return answer
