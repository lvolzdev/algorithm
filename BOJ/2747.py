# 2747 - 피보나치
n = int(input())

start = 0
next = 1
res = 0

if n > 1:
    for i in range(n-1):
        res = start + next # res = 0 + 1 = 1, res = 1 + 1 = 2, res = 1  
        start = next # start = 1, start = 1
        next = res # next = 1, next = 2
elif n == 1:
    res = 1
elif n == 0:
    res = 0

print(res)