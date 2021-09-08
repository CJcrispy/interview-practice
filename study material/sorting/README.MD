# Sorting
- sorting a list of items into ascending or descending order can help find items on that list quickly

## Selection sort
1. Find the smallest card. Swap it with the first card
2. Find the second-smallest card. Swap it with the second card
3. Repeat finding the next smallest card and swapping it into the correct position until the array is sorted

computing summations from 1 to n
```
ex: 
    8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
    (8+1) + (7+2) + (6+3) + (5+4) = 9 + 9 + 9 + 9
                                    = 4 * 9
                                    = 36
```

1. Add the smallest and largest number
2. Multiply by the number of pairs

```
ex:
 5 + 4 + 3 + 2 + 1
 (5+1) + (4+2) + 3
 6 + 6 + 3 = 15 = 6 * 2.5
```
 
 Asymptotic run time for selection sort
 
 The total run time has 3 parts
    1. indexOfMinimum
    - Each individual iteration of the loop takes constant time (n). 
    The number of iterations of this loop is n in the first call, then n-1, then n-2 and so on
    - runtime: Θ(n^2)
    2. swap
    - makes n calls and each call takes constant time
    - runtime: Θ(n)
    3. remainder of the loop
    - testing an incrementing the loop and calling indexOfMinimum & swap
    so that takes constant time for n iterations
    - runtime: Θ(n)

  Total time: n^2/2 + n/2
  Runtime for selection sort: Θ(n^2)

## Insertion sort
- Loop over positions in the array, starting with index 1. 
Insert values in each new position in the array and insert it in the correct place in the subarray

1. Call insert to insert the element that starts at index 1 into the sorted subarray in index 0
2. Call insert to insert the element that starts at index n-1 into the sorted subarray in indices 0 through n-2

run times for insertion sort
- worst case: Θ(n^2)
- best case: Θ(n)
- average case for a random array: Θ(n^2)
- "Almost sorted" case: Θ(n)

## Merge sort
run time:
- worst case: Θ(n*lg*n)
- best case: Θ(n*lg*n)
- average case: Θ(n*lg*n)

    Divide and conquer(Mathematics)
        - breaks a problem into subproblems that are similar to the original problem
        - recursively solves the subproblems, finally combines the solutions to solve the original problem

        1. Divide, the problem into a number of subproblems that are smaller instances of the same problem
        2. Conquer, the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases
        3. Combine, the solutions to the subproblems into the solution for the original problem

How merge sort uses Divide and conquer
1. Divide, by finding the number q of the position midway between p and r. 
Do this step the same way we found the midpoint in binary search: (p + r)/2 and round down
 - divide time: Θ(1)

2. Conquer, by recursively sorting the subarrays in each of the problems created by the divide step.
That is, recursively sort the subarray[p..q] and [q+1...r]
 - conquer time: Θ(n)

3. Combine, by merging the sorted subarrays back into the single sorted subarray [p...r]
 - merge time: Θ(n)


## Quick sort
runtime:
- worst case: Θ(n^2)
- best case: Θ(n*lg*n)
- average case: Θ(n*lg*n)

How quick sort uses divide and conquer
1. Divide, by choosing any element in the sub array [p...r] aka the pivot. 
Rearrange the elements in the array[p...r] that are <= pivot are to its left and all elements >= pivot are to its right aka partioning.

2. Conquer, by recursively sorting the subarrays, array[p...q-1] (left elements) and array[q+1...r] (right elements)

3. Combine, by doing nothing. The array is sorted


## Heap Sort


###### Heap Sort Complexity
```
Time Complexity	 
Best	O(nlog n)
Worst	O(nlog n)
Average	O(nlog n)
Space Complexity	O(1)
Stability	No
```

## Bubble Sort
Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are not in the intended order.

###### sorting elements in ascending order
1. First Iteration (Compare and Swap)
    1. Starting from the first index, compare the first and the second elements.
    2. If the first element is greater than the second element, they are swapped.
    3. Now, compare the second and the third elements. Swap them if they are not in order.
    4. The above process goes on until the last element

2. Remaining Iteration
The same process goes on for the remaining iterations. After each iteration, the largest element among the unsorted elements is placed at the end.

###### Bubble Sort Complexity
```
Time Complexity	 
Best	O(n)
Worst	O(n2)
Average	O(n2)
Space Complexity	O(1)
Stability	Yes
```

## Tree Sort

## Counting Sort


## Bucket Sort


## Radix Sort