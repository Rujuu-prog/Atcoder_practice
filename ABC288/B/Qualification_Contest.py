def main():
    N, K = map(int, input().split())
    s = [input() for i in range(N)]
    s = s[0:K]
    s.sort()
    for i in s:
        print(i)

main()