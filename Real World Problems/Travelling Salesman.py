from sys import maxsize
from itertools import permutations
V = 4
def travellingsalesmanproblem(graph, s):
    vertex =[]
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        current_pathwight = 0

        k = s 
        for j in i:
            current_pathwight += graph[k][j]
            k = j
        current_pathwight += graph[k][s]
        min_path = min(min_path, current_pathwight)
    return min_path

if __name__  == "__main__":

    graph = [[0, 13, 20 , 22], [13, 0 , 35, 15], [20, 35, 0 , 29], [22, 15, 29, 0]]
    s = 0
    print(travellingsalesmanproblem(graph, s))