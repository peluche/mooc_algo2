#!/usr/bin/env python3

import itertools 

def distance(pair):
    """
    the distance between 2 points p and q = sqrt((px - qx)^2 + (py - qy)^2)
    in order to find the closest we don't need an exact distance so we can consider
    the square of the distance as being the distance
    """
    p = pair[0]
    q = pair[1]
    return (p[0] - q[0])**2 + (p[1] - q[1])**2

def bruteforce_closest_pair(points):
    assert(len(points) > 1) # otherwise there is no pair
    closest_p = min(itertools.combinations(points, 2), key=distance)
    return distance(closest_p)

def closest_pair_in_strip(strip, d):
    ds = d
    strip.sort(key=lambda p: p[1])
    for i, p in enumerate(strip):
        for q in strip[i+1:]:
            dist = distance((p, q))
            if (p[1] - q[1])**2 >= ds: break
            if dist < ds:
                ds = dist
    if ds < d:
        return ds
    return ds + 1 # just because i want to know where is the smallest pair

def closest_pair(points):
    """
    the goal is to determine the closest pair of points among a nuage of point in a plan
    using a divide and conquer approach of the problem
    using the bruteforce method for anything smaller than 10 or 15 would give faster results
    """
    if len(points) <= 3:
        return bruteforce_closest_pair(points)
    mid = len(points) // 2
    dl = closest_pair(points[:mid]) # left side
    dr = closest_pair(points[mid:]) # right side
    d = min(dl, dr)
    # construct the middle strip
    strip = []
    mid_point = points[mid]
    for point in points:
        if (point[0] - mid_point[0])**2 < d:
            strip.append(point)
    ds = closest_pair_in_strip(strip, d)
    return min(d, ds)

def closest_pair_wrapper(points):
    """
    the list must be sorted first
    all calculations are made on square so the final result would need to be sqrted
    """
    points.sort()
    return closest_pair(points)

def test(min_val, max_val, nb_points):
    import random
    test_list = []
    for i in range(0, nb_points):
        test_list.append((random.randint(min_val, max_val), random.randint(min_val, max_val)))
    return test_list

def main():
    import time
    tests = [ # (min_val, max_val, nb_points)
        (0, 100, 5),
        (0, 100, 6),
        (0, 100, 15),
        (0, 100, 16),
        (-100, 100, 15),
        (-100, 0, 15),
        (-1000, 1000, 100),
        (-1000, 1000, 1000),
        (-1000, 1000, 3000),
        ]

    for t in tests:
        # kind of crappy test but i'm gonna live with it
        # test the divide and conquer algo with the bruteforce algo
        points = test(*t)
        start = time.time()
        brute_d = bruteforce_closest_pair(points)
        brute_t = time.time() - start
        start = time.time()
        divide_d = closest_pair_wrapper(points)
        divide_t = time.time() - start
        print('bruteforce \t\t{}\ndivide and conquer\t{}'.format(brute_t, divide_t))
        assert(brute_d == divide_d)

if __name__ == '__main__':
    main()
