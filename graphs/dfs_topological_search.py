#!/usr/bin/env python3

explored = {}
current_label = 0

def is_explored(vertex):
    return explored.get(vertex) != None

def explore(vertex):
    explored[vertex] = True

def tag(vertex):
    global current_label
    explored[vertex] = current_label
    current_label -= 1

def dfs(graph, vertex):
    explore(vertex)
    for node in graph[vertex]:
        if not is_explored(node):
            dfs(graph, node)
    tag(vertex)

def dfs_loop(graph):
    """
    generate a topological order of the directed graph
    /!\ graph must be directed, graph shouldn't have any cycle
    """
    for vertex, _ in graph.items():
        if not is_explored(vertex):
            dfs(graph, vertex)

def main():
    """
    A--->B--->D
     `-->C--´
    E--´
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': [],
        'E': ['C'],
        }
    global current_label
    global explored
    explored = {}
    current_label = len(graph)
    dfs_loop(graph)
    print(explored)

if __name__ == '__main__':
    main()
