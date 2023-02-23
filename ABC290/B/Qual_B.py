def main():
    N, K = map(int, input().split())
    S = input()
    count = 0
    count_len = 0
    result = ''
    for s in S:
        result += s
        count_len += 1
        if s == 'o':
            count += 1
            if count == K:
                break
    for i in range(N-count_len):
        result+='x'
    print(result)

main()