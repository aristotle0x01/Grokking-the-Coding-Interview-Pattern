'''
Problem Statement

Topological Sort of a directed graph (a graph with unidirectional edges) is a
linear ordering of its vertices such that for every directed edge (U, V) from
vertex U to vertex V, U comes before V in the ordering.
Given a directed graph, find the topological ordering of its vertices.

Example 1:
Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Example 2:
Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
Output: Following are all valid topological sorts for the given graph:
1) 4, 2, 3, 0, 1
2) 4, 3, 2, 0, 1
3) 4, 3, 2, 1, 0
4) 4, 2, 3, 1, 0
5) 4, 2, 0, 3, 1

Example 3:
Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
Output: Following are all valid topological sorts for the given graph:
1) 5, 6, 3, 4, 0, 1, 2
2) 6, 5, 3, 4, 0, 1, 2
3) 5, 6, 4, 3, 0, 2, 1
4) 6, 5, 4, 3, 0, 1, 2
5) 5, 6, 3, 4, 0, 2, 1
6) 5, 6, 3, 4, 1, 2, 0

There are other valid topological ordering of the graph too.

建立遍历条件dic,对于节点v，如果存在未访问前序节点，则当前路径无效
使用dfs遍历
'''


def topological_sort(num_vertices, edges):
    condition_dic = {}
    graph = {}
    for e in edges:
        condition_dic.setdefault(e[1], []).append(e[0])
        graph.setdefault(e[0], []).append(e[1])

    topological_ordered = []
    visited = [0 for i in range(num_vertices)]
    for k in graph.keys():
        dfs(k, graph, visited, condition_dic, topological_ordered)

        ok = 1
        for v in visited:
            if v == 0:
                ok = 0
                break

        if ok == 1:
            return topological_ordered

    return []


def dfs(k, graph, visited, condition_dic, topological_ordered):
    if visited[k] == 1:
        return

    if k in condition_dic:
        conditions = condition_dic[k]
        for c in conditions:
            if visited[c] == 0:
                return

    visited[k] = 1
    topological_ordered.append(k)

    if k in graph:
        array = graph[k]
        for a in array:
            dfs(a, graph, visited, condition_dic, topological_ordered)

    return


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
