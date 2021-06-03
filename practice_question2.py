'''
Find k closest numbers
Given a sorted number array and two integers ‘K’ and ‘X’,
find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. 
‘X’ is not necessarily present in the array.


Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Input: [2, 4, 5, 6, 9], k = 3, x = 6
Output: [4, 5, 6]
'''

def binary(nums, x):
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + ((end - start) // 2)
        if nums[mid] < x:
            start = mid + 1
        elif nums[mid] > x:
            end = mid - 1
        else:
            return mid
    return start


def k_close(nums, x, k):
    '''
    First, use the binary search algorithm to find the insertion point 
    (The insertion point is the point where the integer 
    x can be placed or inserted within the sorted list). 
    
    The elements before this point are smaller, 
    while the elements after it are greater.
    '''
    no = binary(nums, x)
    '''
    Then, compare the elements around this point to find the k closest numbers.
    '''
    lhs = no - 1
    rhs = no
    while k > 0:
        if lhs < 0 or (rhs < len(nums) and abs(nums[lhs] - x) > abs(nums[rhs] - x)):
            rhs = rhs + 1
        else:
            lhs = lhs - 1
        k = k - 1
    return nums[lhs + 1: rhs]

print(k_close([1,2,3,4,5], 4, 3))
print(k_close([2, 4, 5, 6, 9], 3, 3))