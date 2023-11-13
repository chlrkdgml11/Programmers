answers = [1,2,3,4,5]

A = [1, 2, 3, 4, 5] * (((len(answers)) // 5) + 1)

B = [2, 1, 2, 3, 2, 4, 2, 5] * (((len(answers)) // 8) + 1)

C = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (((len(answers)) // 10) + 1)


result = [0, 0, 0]

for i in range(len(answers)):
    if A[i] == answers[i]:
        result[0] += 1

    if B[i] == answers[i]:
        result[1] += 1

    if C[i] == answers[i]:
        result[2] += 1

M = max(result)
result_student = []

for j in range(len(result)):
    if result[j] == M:
        result_student.append(j+1)

print(result_student)

