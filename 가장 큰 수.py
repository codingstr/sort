# https://programmers.co.kr/learn/courses/30/lessons/42746

def sortSamePlaceValueNums(numbers) :
    # 두 정수를 이어 붙여 return하는 함수
    def concatenateInts(a, b) :
        return int(str(numbers[a])+str(numbers[b]))
    # numbers의 길이가 1 이하거나 0으로만 이루어져 있다면 그대로 return
    if len(numbers) <= 1 or numbers.count(0)==len(numbers) : return numbers
    # numbers의 길이가 2라면 정렬해서 return
    if len(numbers) == 2 : return numbers if concatenateInts(0, 1) >= concatenateInts(1, 0) else list(reversed(numbers))

    pivot, left, right = 0, 1, len(numbers)-1
    while True :
        while left < len(numbers)-1 and concatenateInts(left, pivot) >= concatenateInts(pivot, left) : left += 1
        while right > 0 and concatenateInts(right, pivot) < concatenateInts(pivot, right) : right -= 1
        if left >= right :
            numbers[right], numbers[pivot] = numbers[pivot], numbers[right]
            right, pivot = pivot, right
            break
        numbers[right], numbers[left] = numbers[left], numbers[right]
    # 재귀, pivot의 왼쪽을 정렬한 값 + pivot + pivot의 오른쪽을 정렬한 값을 return
    return sortSamePlaceValueNums(numbers[:pivot]) + [numbers[pivot]] + sortSamePlaceValueNums(numbers[pivot+1:])

def solution(numbers) :
    answer = ''
    
    # numbers가 0으로만 이루어진 경우 처리
    if numbers.count(0)==len(numbers) : answer = '0'
    else :
        # 앞자리수를 기준으로 내림차순 정렬
        numbers.sort(key= lambda num : int(str(num)[0]), reverse=True)
        
        idx = 0
        while idx < len(numbers)-1 :
            # 만약 앞자리수가 같은 number가 있다면 같은 앞자리수를 가진 모든 number를 정렬
            if str(numbers[idx])[0] == str(numbers[idx+1])[0] :
                samePlaceValueIdxs = [i+idx for i, num in enumerate(numbers[idx:]) if str(num)[0]==str(numbers[idx])[0]]
                samePlaceValueNums = [numbers[i] for i in samePlaceValueIdxs]
                numbers = numbers[:samePlaceValueIdxs[0]] + sortSamePlaceValueNums(samePlaceValueNums) + numbers[samePlaceValueIdxs[-1]+1:]

                idx += len(samePlaceValueIdxs)
                continue
            idx += 1
        for num in numbers : answer += str(num)

    return answer

# def test(numbers, answer) :
#     output = solution(numbers)
#     if output == answer : print("correct")
#     else : 
#         print(output)
#         print(answer)

# test([6, 10, 2], "6210")
# test([3, 30, 34, 5, 9], "9534330")
# test([979, 97, 978, 81, 818, 817], "9799797881881817")
# test([67, 676, 677], "67767676")
# test([9, 998], "9998")
# test([1, 10, 100, 1000], "1101001000")
# test([0, 0, 1, 0, 0], "10000")
# test([3021, 30], "303021")
# test([34, 33, 32], "343332")
# test([30, 303], "30330")