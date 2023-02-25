def main():
    N = int(input())
    c = 0
    for n in range(1, N+1):
        if len(str(n))%2 != 0:
            c += 1
    print(c)

main()

