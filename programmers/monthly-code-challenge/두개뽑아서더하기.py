def solution(numbers):
    answer = []
    i = 0
    for a in numbers:
        for b in numbers[i + 1 :]:
            if (a + b) not in answer:
                answer.append(a + b)
        i += 1

    answer.sort()

    return answer
