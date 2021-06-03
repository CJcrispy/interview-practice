'''
First, use the binary search algorithm to find the insertion point (The insertion point is the point where the integer x can be placed or inserted within the sorted list). The elements before this point are smaller, while the elements after it are greater.
Then, compare the elements around this point to find the k closest numbers.
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
    no = binary(nums, x)
    lhs = no - 1
    rhs = no
    while k > 0:
        if lhs < 0 or (rhs < len(nums) and abs(nums[lhs] - x) > abs(nums[rhs] - x)):
            rhs = rhs + 1
        else:
            lhs = lhs - 1
        k = k - 1
    return nums[lhs + 1: rhs]

# Example 1
nums = [8, 10, 12, 15, 18, 20]
k = 4
x = 15
print(k_close(nums, x, k))
# [10, 12, 15, 18]

# Example 2
nums = [4, 6, 8, 9]
k = 3
x = 7
print(k_close(nums, x, k))
# [6, 8, 9]

# Example 3
nums = [2, 3, 5, 6, 7]
k = 1
x = 4
print(k_close(nums, x, k))
# [3]

# Example 4
nums = [5]
k = 1
x = 5
print(k_close(nums, x, k))
# [5]

# Example 5
nums = [10, 11, 12, 13, 15, 16]
k = 1
x = 15
print(k_close(nums, x, k))
# [15]