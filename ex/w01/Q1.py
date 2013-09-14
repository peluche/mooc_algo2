#!/usr/bin/env python3

'''
Question 1
We are given as input a set of n requests (e.g., for the use of an auditorium), with a known start time si and finish time ti for each request i. Assume that all start and finish times are distinct. Two requests conflict if they overlap in time --- if one of them starts between the start and finish times of the other. Our goal is to select a maximum-size subset of the given requests that contains no conflicts. (For example, given three requests consuming the intervals [0,3], [2,5], and [4,7], we want to return the first and third requests.) We aim to design a greedy algorithm for this problem with the following form: At each iteration we select a new request i, including it in the solution-so-far and deleting from future consideration all requests that conflict with i. Which of the following greedy rules is guaranteed to always compute an optimal solution?
- At each iteration, pick the remaining request with the earliest start time.
- At each iteration, pick the remaining request with the earliest finish time.
- At each iteration, pick the remaining request with the fewest number of conflicts with other remaining requests (breaking ties arbitrarily).
- At each iteration, pick the remaining request which requires the least time (i.e., has the smallest value of ti−si) (breaking ties arbitrarily).

i want to compare case 2 and 3
'''

import functools

def conflict(x, y):
    if x[1] < y[0] or y[1] < x[0]:
        return False
    return True

def without_x_and_conflictors(tab, x):
    res = list(tab)
    res.remove(x)
    f = functools.partial(conflict, x)
    res = list(filter(lambda x: not f(x), res))
    return res

def earliest_finish(tab):
    return min(tab, key=lambda x: x[1])

def fewest_conflict(tab):
    min_conflict = len(tab) + 1
    min_conflictor = None

    for e in tab:
        conflicts = 0
        for f in tab:
            if e == f: continue
            if conflict(e, f):
                conflicts += 1
        if conflicts < min_conflict:
            min_conflictor = e
    return min_conflictor

def solve(tab, euristic):
    res = []
    while len(tab) > 0:
        choosen = euristic(tab)
        res.append(choosen)
        tab = without_x_and_conflictors(tab, choosen)
    return res

def test(min_v, max_v, nb_v):
    import random
    res = []
    for i in range(nb_v):
        res.append(sorted([random.randint(min_v, max_v), random.randint(min_v, max_v)]))
    return res

def main():
    tests = test(0, 100, 4)
    print('tests = {}'.format(tests))
    print('earliest finish = {}'.format(solve(tests, earliest_finish)))
    print('fewer conflicts = {}'.format(solve(tests, fewest_conflict)))

if __name__ == '__main__':
    main()
