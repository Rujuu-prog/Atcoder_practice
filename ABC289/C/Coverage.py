import itertools

def main():
    N, M = map(int, input().split())
    s = []
    for i in range(M):
        c = int(input())
        l = list(map(int, input().split()))
        s.append(l)
    collect_l = [k for k in range(1, N+1)]
    pat = []
    for i in range(1, M+1):
        pat += [1 for j in itertools.combinations(s, i) if list(set(sum(list(j), [])))==collect_l]
    print(len(pat))

main()
