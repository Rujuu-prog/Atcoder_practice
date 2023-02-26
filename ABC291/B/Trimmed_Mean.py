def main():
    N = int(input())
    X = list(map(int, input().split()))
    X.sort()
    for i in range(N):
        X.pop(0)
        X.pop(-1)
    result = sum(X)/(5*N-2*N)
    print(result)

main()