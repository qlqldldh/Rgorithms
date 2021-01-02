def solution(nums):
    answer = 0

    lst=[]
    for i in nums:
        if i not in lst:
            lst.append(i)

	return len(nums)/2 if len(lst) >= len(nums) else len(lst)

