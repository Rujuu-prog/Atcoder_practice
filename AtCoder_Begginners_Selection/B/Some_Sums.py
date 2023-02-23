def main():
    N, A, B = map(int, input().split())
    result_sum = 0
    for i in range(N):
        num = str(i+1)
        num_len = len(num)
        num_sum = 0
        for j in range(num_len):
            num_sum += int(num[-(j+1)])
        if A<=num_sum<=B:
            result_sum += i+1
    print(result_sum)

main()
# 改善後(3msだけ速い)
# def main():
#     N, A, B = map(int, input().split())
#     result_sum = 0
#     for i in range(1,N+1):
#         num = str(i)
#         num_sum = 0
#         for j in num:
#             num_sum += int(j)
#         if A<=num_sum<=B:
#             result_sum += i
#     print(result_sum)

# main()
