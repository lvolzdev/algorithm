# 1546 - 평균
n = int(input())
real_score = list(map(int, input().split())) # 한 줄에 여러개 입력받기

real_score.sort() # 오름차순 정렬
max_num = real_score[n-1]

fake_score = []
for i in range(n):
    fake_score.append(real_score[i] / max_num * 100)
    # fake_score[i]에 넣으려고 하면 index error.. append로 추가하니 된다!

print(sum(fake_score)/n)


