import sys

N, M = map(int, sys.stdin.readline().split())

result = []

def dfs():

    if len(result) == M:
        print(' '.join(list(map(str, result))))
        return

    for i in range(1, N + 1):
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()
        