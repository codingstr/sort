# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i in range(len(citations)+1, 1, -1) :
        if len([num for num in citations if num >= i]) >= i :
            answer = i
            break

    return answer

print(solution([3, 0, 6, 1, 5]))