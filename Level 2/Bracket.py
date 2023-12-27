S = ")()("

def solution(S):
    list = []

    answer = True

    for s in S:
        print('s = ', s)
        print('list = ', list)

        if s == '(':
            list.append(s)

        else:
            if len(list) == 0:
                return False
            
            else:
                list.pop()

    if len(list) != 0:
        answer = False
    
    return answer

print(solution(S))
        
