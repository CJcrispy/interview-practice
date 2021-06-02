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
import heapq as hq

def find_closest_element(arr, K, X):
    # TODO: Write your code here
    result = []
    y = (len(arr))
    
    if X <= arr[0]:
        for j in K:
            print(j)
            result.append(arr[j])
    elif X > arr[y - 1]:
        for j in range(K, 0):
            print(j)
            result.append(arr[j])
    print(result)
    return result


find_closest_element([1,2,3,4,5], 4, 6)