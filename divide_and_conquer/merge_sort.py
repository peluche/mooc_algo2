#!/usr/bin/env python3

def join_two_halfs(first_half, second_half):
    i = 0
    j = 0
    res = []
    while 1: # doesn't feel very pythonic, what would be a better way to do that ?
        if i >= len(first_half):
            res += second_half[j:]
            break;
        elif j >= len(second_half):
            res += first_half[i:]
            break;
        elif first_half[i] <= second_half[j]:
            res.append(first_half[i])
            i += 1
        else:
            res.append(second_half[j])
            j += 1
    return res

def count_inversions(l):
    """
    naive merge sort (divide and conquer approach)
    O(n) = n . log(n)
    """
    if len(l) <= 1:
        return l
    # no optimization, list are duplicated
    middle = len(l) // 2
    first_half = count_inversions(list(l[:middle]))
    second_half = count_inversions(list(l[middle:]))
    return join_two_halfs(first_half, second_half)

def main():
    test_lists = [
        [4, 3, 5, 1, 2, 6],
        [],
        [1],
        [1, 2],
        [2, 1],
        [7, 6, 5, 4, 3, 2, 1],
        [6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        ]
    for l in test_lists:
        assert(count_inversions(l) == sorted(l))

if __name__ == '__main__':
    main()
