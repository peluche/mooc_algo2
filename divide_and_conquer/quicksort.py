#!/usr/bin/env python3

def choose_pivot(l, start, stop):
    """
    choose a pivot and swap it in first position
    for this version the pivot is the first value so we do nothing
    could have used random pivot, or mediane
    """
    return l[start]

def quicksort(l, start=-1, stop=-1):
    """
    naive implementation of quicksort
    average n.log(n)
    in place swap
    divide and conquer method
    """
    if start == -1: start = 0
    if stop == -1: stop = len(l)
    size = stop - start
    if size <= 1: return

    pivot = choose_pivot(l, start, stop)
    i = j = start + 1
    while i < stop: # why does it feel dirty to do that in python ? :/
        if l[i] < pivot:
            l[i], l[j] = l[j], l[i] # swap the 2 elements
            j += 1
        i += 1
    j -= 1
    l[start], l[j] = l[j], l[start] # put the pivot in place

    quicksort(l, start, j) # recurse left side
    quicksort(l, j+1, stop) # recurse right side

def test(min_val, max_val, nb_elem):
    import random
    test_list = []
    for i in range(0, nb_elem):
        test_list.append(random.randint(min_val, max_val))
    return test_list

def main():
    tests = [test(0, 100, i) for i in range(10)]
    tests += [test(-1000, 1000, 10**i) for i in range(6)]

    for t in tests:
        quicksort(t)
        assert(t == sorted(t))
        print('.', end="")
    print()

if __name__ == '__main__':
    main()
