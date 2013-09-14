#!/usr/bin/env python3

'''
Question 3
In this programming problem you'll code up Prim's minimum spanning tree algorithm. Download the text file here. This file describes an undirected graph with integer edge costs. It has the format

[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874", indicating that there is an edge connecting vertex #2 and vertex #3 that has cost -8874. You should NOT assume that edge costs are positive, nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph. You should report the overall cost of a minimum spanning tree --- an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Prim's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing a heap-based version. The simpler approach, which should already give you a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge costs). The superior approach stores the unprocessed vertices in the heap, as described in lecture. Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices and their positions in the heap.
'''

def min_of_one_vertex_outside_territory(edges, territory, v):
    try:
        return min([e for e in edges[v] if not e in territory], key=lambda x: edges[v][x])
    except:
        return "key_errorrrrrrrrrrrrrrrrrrrr"
        

def min_of_territory(edges, territory, max_cost):
    return min(territory, key=lambda x: edges[x].get(min_of_one_vertex_outside_territory(edges, territory, x), max_cost))

def solve(edges, start, max_cost):
    '''
    not optimized, should use heap
    '''
    territory = [start]
    costs = []
    end = len(edges)
    while len(territory) < end:
        source = min_of_territory(edges, territory, max_cost)
        dest = min_of_one_vertex_outside_territory(edges, territory, source)
        cost = edges[source][dest]
        territory.append(dest)
        costs.append(cost)
    #     print('cost {} source {} dest {}'.format(cost, source, dest))
    # print('territory {}\nby        {}\ncosts     {}'.format(territory, by, [0] + costs))
    return costs

def main():
    '''
    test with: ./p3.yt < edges.txt
    '''

    max_cost = None
    min_cost = None
    min_coster = None
    edges = {}
    _, n = map(int, input().split())
    for i in range(n):
        source, dest, cost = map(int, input().split())
        if max_cost == None or cost > max_cost: # dirty hack
            max_cost = cost
        if min_cost == None or cost < min_cost:
            min_cost = cost
            min_coster = source

        if not source in edges:
            edges[source] = {}
        if dest in edges[source]:
            edges[source][dest] = min(edges[source][dest], cost)
        else:
            edges[source][dest] = cost

        source, dest = dest, source
        if not source in edges:
            edges[source] = {}
        if dest in edges[source]:
            edges[source][dest] = min(edges[source][dest], cost)
        else:
            edges[source][dest] = cost
    res = solve(edges, min_coster, max_cost + 1)
    res = sum(res)
    print('result {}'.format(res))

if __name__ == '__main__':
    main()
