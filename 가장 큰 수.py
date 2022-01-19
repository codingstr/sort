# https://programmers.co.kr/learn/courses/30/lessons/42746

def sortSamePlaceValueNums(numbers) :


def solution(numbers) :

    answer = ''
    numbers.sort(key= lambda num : int(str(num)[0]), reverse=True)

    if numbers.count(0)==len(numbers) :
        answer = '0'
    else :
        # before

        # idx = 0
        # while idx < len(numbers)-1 :
        #     if str(numbers[idx])[0] == str(numbers[idx+1])[0] :
        #         samePlaceValue = int(str(numbers[idx])[0]) 
        #         samePlaceValueIdxs = sorted([i+idx for i, num in enumerate(numbers[idx:]) if str(num)[0]==str(numbers[idx])[0]], key= lambda i : numbers[i], reverse=True)
                
        #         sortedSamePlaceValueNums = list()
        #         for sortLen in set([len(str(num)) for num in sorted(numbers[min(samePlaceValueIdxs):max(samePlaceValueIdxs)+1], key= lambda num : len(str(num)))]) :
        #             longerNums = [num for num in numbers[min(samePlaceValueIdxs):max(samePlaceValueIdxs)+1] if len(str(num))>=sortLen]
        #             leftNums = sorted([num for num in longerNums if int(str(num)[sortLen-1])>=samePlaceValue], key= lambda num : int(str(num)[sortLen-1]), reverse=True)
        #             rightNums = sorted(list(set(longerNums)-set(leftNums)), reverse=True)
        #             print(longerNums, leftNums, rightNums)
        #             sortedSamePlaceValueNums = leftNums + ([samePlaceValue] if samePlaceValue in numbers else []) + rightNums

        #         numbers = numbers[:min(samePlaceValueIdxs)] + sortedSamePlaceValueNums + numbers[max(samePlaceValueIdxs)+1:]

        #         idx = max(samePlaceValueIdxs)
        #     idx += 1
        # for num in numbers : answer += str(num)

        # after
        
        numbers = sortSamePlaceValueNums(numbers)


    return answer

print(solution([3, 30, 34, 5, 9])+", 9534330")
print(solution([30, 3021])+", 303021")