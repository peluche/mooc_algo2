#!/usr/bin/env python3

'''
Question 1
In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times.. Download the text file here. This file describes a set of jobs with positive and integral weights and lengths. It has the format

[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59. You should NOT assume that edge weights or lengths are distinct.

Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below. 
'''

def solve(jobs):
    return weighted_sum_of_completion(sorted(jobs, key=heuristic))

def main():
    '''
    test with: ./p1.yt < jobs.txt
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
    return (job[1] - job[0], -job[1])

def test_heuristic():
    assert(heuristic([5, 7]) == (2, -7))
    print('.', end='')
    assert(sorted([], key=heuristic) == [])
    print('.', end='')
    assert(sorted([[15, 3], [12, 4]], key=heuristic) == [[15, 3], [12, 4]])
    print('.', end='')
    assert(sorted([[12, 4], [15, 3]], key=heuristic) == [[15, 3], [12, 4]])
    print('.', end='')
    assert(sorted([[12, 4], [10, 2]], key=heuristic) == [[12, 4], [10, 2]])
    print('.', end='')
    assert(sorted([[10, 2], [12, 4]], key=heuristic) == [[12, 4], [10, 2]])
    print('.', end='')

if __name__ == '__main__':
    test_weighted_sum()
    test_heuristic()
    main()
