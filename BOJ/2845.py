# 2845 - 파티가 끝나고 난 뒤
l, p = map(int, input().split())
article = [int(x) for x in input().split()]

num = l * p

for i in range(5):
    cha = article[i] - num
    print(cha, end=' ') # 줄바꿈 없이 출력