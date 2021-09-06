# 1157 - 단어 공부
import collections

answer = []
word = input().upper()
count = collections.Counter(word) # count는 dictionary 형태
max_value = max(list(count.values())) # max() 쓰려면 list여야 함

for key in list(count.keys()):
    if count[key] == max_value:
        answer.append(key)
answer.sort()
if len(answer) != 1:
    print('?')
else:
    print(''.join(answer)) # answer는 list 형태이므로.