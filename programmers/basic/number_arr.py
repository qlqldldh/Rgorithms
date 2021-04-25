def solution(arr, divisor):
    answer = []
    for item in arr:
        if item % divisor != 0:
            continue
        answer.append(item)

    if len(answer) == 0:
        answer,append(-1)

    return sorted(answer)


if __name__ == "__main__":
    arr = map(int, input("elements of array: ").split())
    divisor = int(input("divisor: "))
    #arr = [5, 9, 7, 10]
    #divisor = 5

    answer = solution(arr, divisor)

    print("answer", answer)

