# 1284 - 집 주소

def getWidth(n):
    res = 2 # 양 옆
    while(n):
        tmp = n % 10 # 일의 자리

        if tmp == 0:
            res += 4
        elif tmp == 1:
            res += 2
        else:
            res += 3

        n = n // 10

        if(n):
            res += 1 # 숫자 사이 한 칸

    return res

while True:
    n = int(input()) # 120
    if (n == 0):
        break
    print(getWidth(n))