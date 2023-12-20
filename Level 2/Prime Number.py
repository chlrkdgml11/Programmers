from itertools import permutations
import math

numbers = "123"
numbers_list = list(numbers)

result = []
result += numbers_list

for i in range(2, len(numbers) + 1):
    list_temp = list(permutations(numbers_list, i))
    result += list_temp

answer = []

for i in range(len(result)):
    result_temp = ''
    for j in range(len(result[i])):
        result_temp += result[i][j]
    
    answer.append(int(result_temp))

temp_cnt = []

answer = list(set(answer))

for x in answer:
    if x == 0 or x == 1:
        continue

    if x == 2:
        temp_cnt.append(x)
        continue

    if x % 2 == 0:
        continue

    cnt = 0
    print('    x = ', x)
    for y in range(2, int(math.sqrt(x)) + 1):
        if x % y == 0:
            cnt = 1
            continue
    if cnt == 0:
        temp_cnt.append(x)

print(temp_cnt)
print(len(set(temp_cnt)))
