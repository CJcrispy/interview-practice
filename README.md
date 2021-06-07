# interview-practice
 
## Algorithms

Algorithmic Complexity
- a measure of how long an algorithm would take to complete given an input size of n

How do you measure the efficiency of an algorithm?
- Asymptotic Analysis: which allows algorithms to be compared independently 
of a particular programming language or hardware

###### Binary Search
- an efficient algorithm for finding an item from a sorted list of items

ex: Searching an item in a list by name
    1. min = 0 and max = n-1
    2. compute the average rounded down
    3. if array[guess] = target, then stop
    4. if guess is too low set min = guess + 1
    5. if guess is too high set max = guess - 1
    6. step 2

- runtime for binary search: log2(n) + 1 (for most guesses)

## Asymptotic notation
- by dropping the less significant terms and the constant coefficients, 
we can focus on the important part of an algorithm's run time it rate of growth

- 3 forms of asymptotic notation
    - big - Θ notation (Big Theta)
    - big - O
    - big - Ω notation (Big Omega)

###### Functions in asymptotic notation

log(a)n = log(b)n / log(b)a  (All positive numbers for a, b, n)

- if a and b are constants, then log(a)n and log(b)n differ only by a factor of log(b)a, 
a constant factor can be ignored in asymptotic notation

- Θ(log(a)n) is the worst case run time for binary search, for any positive constan a

- There is an order to functions used when analyzing algorithms using asymptotic notation
 - if a and b are constants a < b, then a run time of Θ(n^a) grows more slowly than a run time of Θ(n^b)

- functions in Asymptotic notation(slowest - fastest)
 - Θ(1)
 - Θ(log(2)n)
 - Θ(n)
 - Θ(n*log(2)n)
 - Θ(n^2)
 - Θ(n^2*log(2)n)
 - Θ(n^3)
 - Θ(2^n)
 - Θ(n!)
- note: an exponential function a^n, where a > 1, grows faster than any polynomial function n^b, where b is any constant

###### big - Θ notation (Big Theta)
- Θ(n) = once n gets large enough, the running time is at least k1 * n and at most k2 * n  from some constants k1 and k2
    - once large enough the run time is between k1 * f(n) and k2 * f(n)

- When we use big - Θ notation,  we're saying that we have an asymptotically tight bound on the running time (large values on n)

###### big - O notation
- used for asymptotic upper bonds
- we can say that a run time of Θ(f(n)) in a particular situation is also O(f(n))
 - The converse is not necessarily true, a binary search can run in O(log(2)n) but not Θ(log(2)n)

###### big - Ω notation (Big Omega)
- used for asymptotic lower bounds


## Sorting
- sorting a list of items into ascending or descending order can help find items on that list quickly

###### Selection sort
1. Find the smallest card. Swap it with the first card
2. Find the second-smallest card. Swap it with the second card
3. Repeat finding the next smallest card and swapping it into the correct position until the array is sorted

computing summations from 1 to n
ex: 
 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1
 (8+1) + (7+2) + (6+3) + (5+4) = 9 + 9 + 9 + 9
                               = 4 * 9
                               = 36
                               
1. Add the smallest and largest number
2. Multiply by the number of pairs

ex:
 5 + 4 + 3 + 2 + 1
 (5+1) + (4+2) + 3
 6 + 6 + 3 = 15 = 6 * 2.5
 
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
