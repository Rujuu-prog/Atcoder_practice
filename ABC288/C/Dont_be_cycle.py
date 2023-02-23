import collections
import itertools

# def main():
#     N, M = map(int, input().split())
#     li = sum([list(map(int, input().split())) for i in range(M)], [])
#     print(max(collections.Counter(li).values())-1)

# main()


def main():
    N, M = map(int, input().split())
    A = collections.Counter(itertools.chain.from_iterable([list(map(int, input().split())) for i in range (M)]))
    result_len = len([1 for v in A.values() if v > 1])
    print(result_len//3)

main()

# unionfind木を使うらしい