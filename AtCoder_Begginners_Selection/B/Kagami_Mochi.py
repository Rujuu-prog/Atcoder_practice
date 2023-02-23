def main():
    N = int(input())
    l = [int(input()) for i in range(N)]
    l_seted = set(l)
    print(len(l_seted))

main()