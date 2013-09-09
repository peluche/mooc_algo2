#!/usr/bin/env python3

import random

def choose_pivot(l, start, stop):
    """
    choose a pivot at random and swap it in first position
    """
    x = random.randint(start, stop - 1)
    l[start], l[x] = l[x], l[start]
    return l[start]

def rselect(l, rank, start=-1, stop=-1):
    """
    select the n-th ranked element in a non-sorted list
    ranks start at 0
    O(n) = n  in average (quicksort-ish)
    """
    if start == -1: start = 0
    if stop == -1: stop = len(l)
    size = stop - start
    if rank >= size: return None # impossible

    pivot = choose_pivot(l, start, stop)
    i = j = start + 1
    while i < stop:
        if l[i] < pivot:
            l[j], l[i] = l[i], l[j]
            j += 1
        i += 1
    j -= 1
    l[start], l[j] = l[j], l[start]

    pivot_rank = j - start
    if pivot_rank == rank:  # found the n-th rank
        return l[j]
    elif pivot_rank > rank: # recurse on left part
        return rselect(l, rank, start, j)
    else:                   # recurse on right part
        return rselect(l, rank - (pivot_rank + 1), j+1, stop)

def test(min_val, max_val, nb_elem):
    import random
    test_list = []
    for i in range(0, nb_elem):
        test_list.append(random.randint(min_val, max_val))
    return test_list

def main():
    tests = [test(0, 100, i) for i in range(1, 100)]
    tests += [test(-1000, 1000, 10**i) for i in range(5)]

    for t in tests:
        rank = random.randint(0, len(t) - 1)
        assert(rselect(t, rank) == sorted(t)[rank])
        print('.', end='')
    print()

if __name__ == '__main__':
    main()
