# https://programmers.co.kr/learn/courses/30/lessons/42746

def sortSamePlaceValueNums(numbers) :
    # 두 정수를 이어 붙여 return하는 함수
    def concatenateInts(a, b) :
        return int(str(a)+str(b))
    # numbers의 길이가 1 이하거나 0으로만 이루어져 있다면 그대로 return
    if len(numbers) <= 1 or numbers.count(0)==len(numbers) : return numbers
    # pivot의 앞과 뒤에 이어 붙였을 때를 비교해 leftSide와 rightSide로 분류
    pivot = numbers[0]
    tail = numbers[1:]
    leftSide = [num for num in tail if concatenateInts(num, pivot) > concatenateInts(pivot, num)]
    # rightSide = list(set(numbers)-set([pivot])-set(leftSide))
    rightSide = [num for num in tail if concatenateInts(num, pivot) <= concatenateInts(pivot, num)]
    # 재귀, leftSide를 정렬한 값 + pivot + rightSide를 정렬한 값을 return
    return sortSamePlaceValueNums(leftSide) + [pivot] + sortSamePlaceValueNums(rightSide)

def solution(numbers) :

    answer = ''
    numbers.sort(reverse=True)
    # numbers를 앞자리수를 기준으로 내림차순 정렬
    numbers.sort(key= lambda num : int(str(num)[0]), reverse=True)
    # numbers가 0으로만 이루어진 경우 처리
    if numbers.count(0)==len(numbers) : answer = '0'
    else :
        idx = 0
        while idx < len(numbers)-1 :
            # 만약 앞자리수가 같은 number가 있다면 같은 앞자리수를 가진 모든 number를 sortSamePlaceValueNums로 정렬
            if str(numbers[idx])[0] == str(numbers[idx+1])[0] :
                samePlaceValueIdxs = [i+idx for i, num in enumerate(numbers[idx:]) if str(num)[0]==str(numbers[idx])[0]]
                samePlaceValueNums = [numbers[i] for i in samePlaceValueIdxs]
                numbers = numbers[:samePlaceValueIdxs[0]] + sortSamePlaceValueNums(samePlaceValueNums) + numbers[samePlaceValueIdxs[-1]+1:]

                idx += len(samePlaceValueNums)
                continue
            idx += 1
        for num in numbers : answer += str(num)

    return answer

def test(numbers, answer) :
    output = solution(numbers)
    if output == answer : print("correct")
    else : 
        print(output)
        print(answer)

test([6, 10, 2], "6210")
test([3, 30, 34, 5, 9], "9534330")
test([979, 97, 978, 81, 818, 817], "9799797881881817")
test([67, 676, 677], "67767676")
test([9, 998], "9998")
test([1, 10, 100, 1000], "1101001000")
test([0, 0, 1, 0, 0], "10000")
test([3021, 30], "303021")
test([34, 33, 32], "343332")