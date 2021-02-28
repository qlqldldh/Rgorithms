import sys

t = int(input())


def check():
    for i in range(len(a)-1):
        if a[i] == a[i+1][0:len(a[i])]:
            print('NO')
            return
    print('YES')


for _ in range(t):
    n = int(input())
    a = []
    for i in range(n):
        a.append(sys.stdin.readline().strip())  # 시간초과 방지를 위해 sys 사용
    a.sort()
    check()
