# AC

import collections

def main():
    N = int(input())
    S = [1 if input()=='For' else 0 for i in range(N)]
    c = collections.Counter(S)
    if c[1] > N//2:
        print('Yes')
    else:
        print('No')

main()

