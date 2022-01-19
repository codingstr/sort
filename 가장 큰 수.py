# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers) :

    answer = ''
    numbers.sort(reverse=True)
    numbers.sort(key= lambda num : int(str(num)[0]), reverse=True)

    if numbers.count(0)==len(numbers) :
        answer = '0'
    else :
        idx = 0
        while idx < len(numbers)-1 :
            if str(numbers[idx])[0] == str(numbers[idx+1])[0] :
                samePlaceValueNums = [num for num in numbers[idx:] if str(num)[0]==str(numbers[idx])[0]]
                maxNumLen = len(str(max(samePlaceValueNums)))
                samePlaceValueNums.sort(key= lambda num : int(str(num)+str(numbers[idx])[0]*(maxNumLen-len(str(num)))), reverse=True)
                sortedSamePlaceValueIdxs = [numbers.index(num) for num in samePlaceValueNums]
                numbers = numbers[:min(sortedSamePlaceValueIdxs)] + samePlaceValueNums + numbers[max(sortedSamePlaceValueIdxs)+1:]

                idx += len(samePlaceValueNums)
                continue
            idx += 1
        for num in numbers : answer += str(num)

    return answer

print(solution([979, 97, 978, 81, 818, 817]))
print('9799797881881817')
print(solution([67, 676, 677]))
print('67767676')