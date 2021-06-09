'''
3. Sum of two values

Given an array of integers and a value, 
determine if there are any two integers in the array whose sum is 
equal to the given value. 

Return true if the sum exists and return false if it does not.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

def sum(arr, val):
 #TODO: Write - Your - Code
    for i in arr:
        diff = val - i
        if diff in arr:
            print([arr.index(i), arr.index(diff)])
            return True
    return False

print(sum([2, 7, 11, 15], 9))
# print(sum([1, 5, 133, 20], 25))
# print(sum([0, 24, 42, 12], 36))
print(sum([3, 7, 1, 2, 8, 4, 5], 9))
