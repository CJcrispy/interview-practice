from sys import maxsize
from itertools import permutations

# number of nodes
V = 4

# implementation of traveling Salesman Problem
# graph = MST
# s = starting position
def travellingSalesman(graph, s):

    # store all vertex apart from source
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minium weight using Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current path weight(cost)
        current_pathweight = 0

        # compute current path weight
        # k = current position
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

    return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(travellingSalesman(graph, s))