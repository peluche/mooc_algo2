'''
Question 1
We are given as input a set of n requests (e.g., for the use of an auditorium), with a known start time si and finish time ti for each request i. Assume that all start and finish times are distinct. Two requests conflict if they overlap in time --- if one of them starts between the start and finish times of the other. Our goal is to select a maximum-size subset of the given requests that contains no conflicts. (For example, given three requests consuming the intervals [0,3], [2,5], and [4,7], we want to return the first and third requests.) We aim to design a greedy algorithm for this problem with the following form: At each iteration we select a new request i, including it in the solution-so-far and deleting from future consideration all requests that conflict with i. Which of the following greedy rules is guaranteed to always compute an optimal solution?
- At each iteration, pick the remaining request with the earliest start time.
- At each iteration, pick the remaining request with the earliest finish time.
- At each iteration, pick the remaining request with the fewest number of conflicts with other remaining requests (breaking ties arbitrarily).
- At each iteration, pick the remaining request which requires the least time (i.e., has the smallest value of ti−si) (breaking ties arbitrarily).
'''

[0, 3], [2, 5], [4, 7] # 1 work, 2 work, 3 work, 4 fail (if we break tie arbitrarily we can choose [2, 5]
[0, 4], [3, 6], [5, 10] # 4 fail no matter ties
[0, 100], [1, 2], [3, 4] # 1 fail, 2 work, 3 work
[0, 100] [101, 102], [102, 103] # 2 work, 3 work
[5, 8], [10, 100], [7, 9], [8, 10]
[9, 34], [38, 39], [60, 90], [31, 40]   # voir Q1.py
                                        # earliest finish = [[9, 34], [38, 39], [60, 90]]
                                        # fewer conflicts = [[31, 40], [60, 90]] #=> 3 fail !

# answer 2: earliest finish time

'''
Question 2
We are given as input a set of n jobs, where job j has a processing time pj and a deadline dj. Recall the definition of completion times Cj from the video lectures. Given a schedule (i.e., an ordering of the jobs), we define the lateness lj of job j as the amount of time Cj−dj after its deadline that the job completes, or as 0 if Cj≤dj. Our goal is to minimize the maximum lateness, maxjlj. Which of the following greedy rules produces an ordering that minimizes the maximum lateness? You can assume that all processing times and deadlines are distinct.
- None of the above.
- Schedule the requests in increasing order of deadline dj
- Schedule the requests in increasing order of the product dj⋅pj
- Schedule the requests in increasing order of processing time pj
'''

[3, 5]  # pj = processing time = 3
        # dj = dead line = 5

[4, 5], [5, 6], [1, 7]  # 2 [4, 5], [5, 6], [1, 7] #=> 0, 3, 3 = 3
                        # 3 [1, 7], [4, 5], [5, 6] #=> 0, 0, 4 = 4 <-- fail 
                        # 4 [1, 7], [4, 5], [5, 6] #=> 0, 0, 4 = 4 <-- fail

[3, 3], [4, 7], [1, 8]  # 2 [3, 3], [4, 7], [1, 8] #=> 0, 0, 0 = 0
                        # 3 [1, 8], [3, 3], [4, 7] #=> 0, 1, 1 = 1 <-- fail
                        # 4 [1, 8], [3, 3], [4, 7] #=> 0, 1, 1 = 1 <-- fail

# answer 2: increasing order of deadline

'''
Question 3
Consider an undirected graph G=(V,E) where every edge e∈E has a given cost ce. Assume that all edge costs are positive and distinct. Let T be a minimum spanning tree of G and P a shortest path from the vertex s to the vertex t. Now suppose that the cost of every edge e of G is increased by 1 and becomes ce+1. Call this new graph G′. Which of the following is true about G′?
- T may not be a minimum spanning tree and P may not be a shortest s-t path.
- T is always a minimum spanning tree and P is always a shortest s-t path.
- T may not be a minimum spanning tree but P is always a shortest s-t path.
- T must be a minimum spanning tree but P may not be a shortest s-t path.
'''

A--[1]--B--[1]--C--[1]--D       # the shortest path from A to D is [A, B, C, D] = 3
`--------[4]------------´       # after increating all edges from 1 the shortest path from A to D is [A, D] = 5 <-- 2 and 3 fail

# to calculate the minimum spanning tree we choose the smallest edge of the frontier, add his node to the territory, rince and repeat
# so adding 1 to all doesn't change the property of the MST

# answer 4 T must be a MST

'''
Question 4
Suppose T is a minimum spanning tree of the graph G. Let H be an induced subgraph of G. (I.e., H is obtained from G by taking some subset S⊆V of vertices, and taking all edges of E that have both endpoints in S.) Which of the following is true about the edges of T that lie in H? You can assume that edge costs are distinct, if you wish.
- They might have non-empty intersection with a minimum spanning tree TH of H, but at least one of the edges will be missing from TH
- They form a minimum spanning tree of H
- They are always contained in some minimum spanning tree of H
- They might be disjoint from every minimum spanning tree of H
'''
                              
# MST: [A, B], [B, C], [C, D]
 A--[1]--B                     A--[1]--B  # we keep the vertices A, B, D
 |       |                     |          # [A, B] is not a MST #=> 2 is false
[4]     [2]                   [4]                         
 |       |                     |                          
 D--[3]--C                     D                          

# answer 3

'''
Question 5
Consider an undirected graph G=(V,E) where edge e∈E has cost ce. A minimum bottleneck spanning tree T is a spanning tree that minimizes the maximum edge cost maxe∈Tce. Which of the following statements is true? Assume that the edge costs are distinct.
- A minimum bottleneck spanning tree is always a minimum spanning tree but a minimum spanning tree is not always a minimum bottleneck spanning tree.
- A minimum bottleneck spanning tree is not always a minimum spanning tree and a minimum spanning tree is not always a minimum bottleneck spanning tree.
- A minimum bottleneck spanning tree is always a minimum spanning tree and a minimum spanning tree is always a minimum bottleneck spanning tree.
- A minimum bottleneck spanning tree is not always a minimum spanning tree, but a minimum spanning tree is always a minimum bottleneck spanning tree.
'''

 A--[1]--B--[2]--C--[9]--D # MST: [A, B], [B, C], [C, D]
  `-----[3]-----´          # possible MBST: [A, B], [A, C], [C, D] #=> 1 and 3 are false

# answer 4
