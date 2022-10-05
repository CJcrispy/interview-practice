# Algorithms

Algorithmic Complexity
- a measure of how long an algorithm would take to complete given an input size of n

How do you measure the efficiency of an algorithm?
- Asymptotic Analysis: which allows algorithms to be compared independently 
of a particular programming language or hardware

## Binary Search
- an efficient algorithm for finding an item from a sorted list of items
```
ex: Searching an item in a list by name
    1. min = 0 and max = n-1
    2. compute the average rounded down
    3. if array[guess] = target, then stop
    4. if guess is too low set min = guess + 1
    5. if guess is too high set max = guess - 1
    6. step 2
```

- runtime for binary search: log2(n) + 1 (for most guesses)


## Dijkstra's algorithm
- given a grpah and a source vertex, find shortest paths from source to all vertices in the given graph

1) Create a set sptSet (Shortest path tree) that keeps track of vertices included in spt whose minimum distance from source is calculated and finalized

2) Assign a distance value to all vertices in the input graph . Initialize all distance values as INFINITE. Assign distance values as 0 for the source vortex so that its is picked first

3) while sptSet doesn't include all vertices
    a) Pick a vertex, u, which is not there in sptSet and has minimum distance
    b) include u to sptSet
    c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex, v, if sum of distance value aof u and weight of edge u-v, is less than the distance value of v, then update the distance value of v


## A* algorithm

###### What is A* Search Algorithm? 
- A* Search algorithm is one of the best and popular technique used in path-finding and graph traversals.

1) Intitialize the open list

2) Intitialize the closed list (put the starting node on the open list)
    - you can leave its "F" value at 0

3) whilte the open list is not empty:
    a) find the node with the least "f" value on the open list, call it "q"
    b) pop "q" off the open list
    c) generate q's 8 successors and set their parents to q
    d) for each successor
        i) if successor is the goal, stop search
        ii) else, compute both g and h for successor
          successor.g = q.g + distance between successor and q
          successor.h = distance from goal to 
          successor (This can be done using many 
          ways, we will discuss three heuristics- 
          Manhattan, Diagonal and Euclidean 
          Heuristics)
          successor.f = successor.g + successor.h
        iii) if a node with the same position as 
            successor is in the OPEN list which has a 
           lower f than successor, skip this successor
        iV) if a node with the same position as 
            successor  is in the CLOSED list which has
            a lower f than successor, skip this successor
            otherwise, add  the node to the open list
        end (for loop)
    e) push q on the closed list
    end (while loop)


# Asymptotic notation
- by dropping the less significant terms and the constant coefficients, 
we can focus on the important part of an algorithm's run time it rate of growth

- 3 forms of asymptotic notation
    - big - Θ notation (Big Theta)
    - big - O
    - big - Ω notation (Big Omega)

## Functions in asymptotic notation

log(a)n = log(b)n / log(b)a  (All positive numbers for a, b, n)

- if a and b are constants, then log(a)n and log(b)n differ only by a factor of log(b)a, 
a constant factor can be ignored in asymptotic notation

- Θ(log(a)n) is the worst case run time for binary search, for any positive constant a

- There is an order to functions used when analyzing algorithms using asymptotic notation
  if a and b are constants a < b, then a run time of Θ(n^a) grows more slowly than a run time of Θ(n^b)

```
functions in Asymptotic notation(slowest - fastest)
    - Θ(1)
    - Θ(log(2)n)
    - Θ(n)
    - Θ(n*log(2)n)
    - Θ(n^2)
    - Θ(n^2*log(2)n)
    - Θ(n^3)
    - Θ(2^n)
    - Θ(n!)
```
- note: an exponential function a^n, where a > 1, grows faster than any polynomial function n^b, where b is any constant

## big - Θ notation (Big Theta)
- Θ(n) = once n gets large enough, the running time is at least k1 * n and at most k2 * n  from some constants k1 and k2
    - once large enough the run time is between k1 * f(n) and k2 * f(n)

- When we use big - Θ notation,  we're saying that we have an asymptotically tight bound on the running time (large values on n)

## big - O notation
- used for asymptotic upper bonds
- we can say that a run time of Θ(f(n)) in a particular situation is also O(f(n))
 - The converse is not necessarily true, a binary search can run in O(log(2)n) but not Θ(log(2)n)

## big - Ω notation (Big Omega)
- used for asymptotic lower bounds
