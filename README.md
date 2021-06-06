# interview-practice
 
## Algorithms

Algorithmic Complexity
    - a measure of how long an algorithm would take to complete given an input size of n

    How do you measure the efficiency of an algorithm?
    - Asymptotic Analysis: which allows algorithms to be compared independently of a particular programming language or hardware

Binary Search
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
    - by dropping the less significant terms and the constant coefficients, we can focus on the important part of an algorithm's run time it rate of growth

    - 3 forms of asymptotic notation
        - big - Θ notation (Big Theta)
        - big - O
        - big - Ω notation (Big Omega)

    ###### Functions in asymptotic notation

    log(a)n = log(b)n / log(b)a  (All positive numbers for a, b, n)

    - if a and b are constants, then log(a)n and log(b)n differ only by a factor of log(b)a, a constant factor can be ignored in asymptotic notation

    - 

    ###### big - Θ notation (Big Theta)
        - Θ(n) = once n gets large enough, the running time is at least k1 * n and at most k2 * n  from some constants k1 and k2
            - once large enough the run time is between k1 * f(n) and k2 * f(n)

        - When we use big - Θ notation,  we're saying that we have an asymptotically tight bound on the running time (large values on n)
