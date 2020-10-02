#!/bin/python3
import os


def sockMerchant(n, ar):
    pair_count = 0
    ar_unique = list()
    for sock in ar:
        if sock not in ar_unique:
            ar_unique.append(sock)
        else:
            ar_unique.remove(sock)
            pair_count += 1

    return pair_count


if __name__ == '__main__':
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    n = 9
    result = sockMerchant(n, ar)
    print(result)

    # HackerRank
    """fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()"""
