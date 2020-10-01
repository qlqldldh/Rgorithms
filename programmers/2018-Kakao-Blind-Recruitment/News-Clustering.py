# Programmers - 2018 Kakao Blind Recruitment - News Clustering


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    cmn = 0

    strlst1 = []
    strlst2 = []

    temp = ""
    # strlst1
    for i in range(len(str1)):
        if str1[i].isalpha():
            temp += str1[i]
        else:  # alphabet이 아닌 경우 짝이 이루어질 수 없음 -> 그냥 초기화
            temp = ""
        if len(temp) == 2:
            strlst1.append(temp)
            temp = temp[1:]  # pollFirst from the string

    temp = ""
    # strlst2
    for i in range(len(str2)):
        if str2[i].isalpha():
            temp += str2[i]
        else:
            temp = ""
        if len(temp) == 2:
            if temp in strlst1:  # 합집합 = 집합1 + 교집합 원소가 빠진 집합2
                cmn += 1
                strlst1.remove(temp)  # python은 list에서 remove 시 가장 앞 놈부터 사라짐
            strlst2.append(temp)
            temp = temp[1:]

    # Result
    if len(strlst2) + len(strlst1) == 0: return 65536  # 분모가 0 -> 65536
    elif cmn==0: return 0  # 분자가 0 -> 0
    else: return int(cmn / (len(strlst2) + len(strlst1)) * 65536)
