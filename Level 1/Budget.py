d = [2,2,3,3]
budget = 10

d.sort()

print(d)

answer = 0

for i in range(len(d)):
    if budget - d[i] >= 0:
        answer += 1
        budget -= d[i]

print(answer)