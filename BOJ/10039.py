# 10039 - 평균 점수

nums = [int(input()) for _ in range(5)] # 5줄에 정수 입력 받기

res = 0
for i in range(5):
    if nums[i] < 40:
        nums[i] = 40
    res += nums[i]

print(int(res / 5))