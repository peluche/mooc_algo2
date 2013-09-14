#!/usr/bin/env python3

'''
Question 2
For this problem, use the same data set as in the previous problem. Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
'''

def solve(jobs):
    return weighted_sum_of_completion(sorted(jobs, key=heuristic))

def main():
    '''
    test with: ./p2.yt < jobs.txt
    '''
    jobs = []
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        jobs.append([x, y])
    res = solve(jobs)
    print('result {}'.format(res))

def weighted_sum_of_completion(res):
    total = 0
    completion = 0
    for r in res:
        completion += r[1]
        total += completion * r[0]
    return total

def test_weighted_sum():
    assert(weighted_sum_of_completion([]) == 0)
    print('.', end='')
    assert(weighted_sum_of_completion([[23, 45]]) == 1035)
    print('.', end='')
    assert(weighted_sum_of_completion([[1, 4], [7, 3], [9, 12]]) == 4+49+171)
    print('.', end='')
    assert(weighted_sum_of_completion([[9, 12], [1, 4], [7, 3]]) == 108+16+133)
    print('.', end='')

def heuristic(job):
    return -job[0] / job[1]

def test_heuristic():
    assert(heuristic([5, 7]) == -5/7)
    print('.', end='')
    assert(sorted([], key=heuristic) == [])
    print('.', end='')
    assert(sorted([[15, 3], [12, 4]], key=heuristic) == [[15, 3], [12, 4]])
    print('.', end='')
    assert(sorted([[12, 4], [15, 3]], key=heuristic) == [[15, 3], [12, 4]])
    print('.', end='')
    assert(sorted([[12, 4], [10, 2]], key=heuristic) == [[10, 2], [12, 4]])
    print('.', end='')
    assert(sorted([[10, 2], [12, 4]], key=heuristic) == [[10, 2], [12, 4]])
    print('.', end='')

if __name__ == '__main__':
    test_weighted_sum()
    test_heuristic()
    main()
