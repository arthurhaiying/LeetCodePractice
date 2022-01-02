from typing import AnyStr, List, Dict, Tuple, Optional, TypeVar


""" Given an array of numbers, find the pair (i, j) such that nums[i] <= nums[j] 
    and j - i is maxmized """


def maxWidthRamp_baseline(nums: List[int]) -> int:
    answer = [0]*len(nums)
    for i,x in enumerate(nums):
        width = 0
        for j in range(i+1, len(nums)):
            if nums[j] >= i:
                width = j - i
        answer[i] = width
    return max(answer)


def maxWidthRamp1(nums: List[int]) -> int:
    # for each i, find the maximal-width ramp ending at nums[i]
    # iterate array from left to right and maintains a monotonously decreasing stack
    # if next element < s.top, add element to stack
    # if next element >= s.top, find the first element in stack that is greater than next element by binary search
    answer = [0]*len(nums)
    stack = []
    for i,x in enumerate(nums):
        if not stack or x < stack[-1][0]:
            stack.append((x,i))
        else: 
            idx = first_greater_than(stack, 0, len(stack), x)
            j = stack[idx+1][1]
            #print("i: {} j: {}".format(i, j))
            width = i - j
            answer[i] = width

    return max(answer)

            
Entry = Tuple[int, int]      

#import pdb

def first_greater_than(arr: List[Entry], l: int, r: int, x: int) -> int:
    # assume arr is decreasing
    #pdb.set_trace()
    if l == r: 
        # empty array
        return -1 
    mid = (l + r) // 2
    if arr[mid][0] > x and (mid+1 == r or arr[mid+1][0] <= x):
        return mid
    elif arr[mid][0] > x and arr[mid+1][0] > x:
        return first_greater_than(arr, mid, r, x)
    else: # arr[mid][0] <= x
        return first_greater_than(arr, l, mid, x)

import random,timeit


def maxWidthRamp2(nums: List[int]) -> int:
    # iterate forwards and only keep decreasing values (which should be used as left ends) in a stack
    # iterate backwards (right ends) against the stack
    stack = []
    for i,x in enumerate(nums):
        if i == 0 or nums[i] < stack[-1][0]:
            stack.append((x, i))

    answer = [0]*len(nums)
    for j in range(len(nums)-1,-1,-1):
        y = nums[j]
        width = 0
        while stack and y >= stack[-1][0]:
            left, i = stack.pop()
            width = j - i
        answer[j] = width
    return max(answer)


            


if __name__ == '__main__':
    nums = [9,8,7,6,5,5,4,3,1,0]
    result = maxWidthRamp1(nums)
    print("Result: {}".format(result))
    nums1 = [6,0,8,2,1,5]
    result = maxWidthRamp1(nums1)
    print("Result: {}".format(result))
    nums2 = [9,8,1,0,1,9,4,0,4,1]
    result2 = maxWidthRamp1(nums2)
    print("Result 2: {}".format(result2))
    # big_nums = [random.randint(1, 1000) for x in range(100000)]
    # time0 = timeit.timeit(lambda: maxWidthRamp_baseline(big_nums), number=1)
    # print("time0: {:3f}".format(time0))
    # time1 = timeit.timeit(lambda: maxWidthRamp1(big_nums), number=1)
    # print("time 1: {:3f}".format(time1))



    
       




        

