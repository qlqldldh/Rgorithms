def solution(nums):
    answer = 0

    lst=[]
    for i in nums:
        if i not in lst:
            lst.append(i)
    
    if len(lst)>=len(nums)/2 : answer=len(nums)/2
    else : answer=len(lst)

    return answer
