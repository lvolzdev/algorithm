# 2309 - 일곱 난쟁이
h = [int(input()) for _ in range(9)]

num1, num2 = 0, 0

for i in range(9):
    for j in range(i+1, 9):
        if sum(h) - (h[i] + h[j]) == 100:
            num1 = h[i]
            num2 = h[j]

h.remove(num1)
h.remove(num2)

h.sort() # 리스트 오름차순 정렬
print('\n'.join(map(str, h))) # 배열 원소 하나씩 줄 바꿈 출력


# 9개 중에서 7개 골라서 그 합이 100이 되는 경우를 찾는 문제.
# 7개 고르는 것 보다 모두 다 더하고 2개 빼는 게 더 쉬움..!