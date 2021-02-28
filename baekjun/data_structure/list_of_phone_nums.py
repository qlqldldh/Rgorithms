import sys


def check(_phone_nums):
    for i in range(len(_phone_nums) - 1):
        if _phone_nums[i] == _phone_nums[i + 1][0:len(_phone_nums[i])]:
            print('NO')
            return
    print('YES')


def solution():
    t = int(input())

    for _ in range(t):
        n = int(input())
        phone_nums = []
        for _ in range(n):
            phone_nums.append(sys.stdin.readline().strip())  # 시간초과 방지를 위해 sys 사용
        phone_nums.sort()
        check(phone_nums)
