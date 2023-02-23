def main():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0
    for i in b:
        result += a[i-1]
    print(result)

main()
