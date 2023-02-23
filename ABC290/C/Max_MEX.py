# import itertools

# def cal(A, K):
#     B = set(itertools.combinations(A, K))
#     collect_li = [i for i in range(K)]
#     max = 0
#     # l = [set(collect_li) - set(i) for i in B]
#     # print(l)
#     for i in B:
#         result_li = set(collect_li) - set(i)
#         if not result_li:
#             print(K)
#             return
#         re_min = min(result_li)
#         if max < re_min:
#             max = re_min
#     print(max)


# def main():
#     N, K = map(int, input().split())
#     A_o = list(map(int, input().split()))
#     A = [i for i in A_o if i <= K]
#     if not A:
#         print(0)
#         return
#     elif len(A)<K:
#         cal(A, len(A))
#     else:
#         cal(A,K)

# main()

# def main():
#     N, K = map(int, input().split())
#     A = list(map(int, input().split()))
#     A.sort()
#     collect_li = [i for i in range(K)]
#     result_li = list(set(collect_li) ^ set(A))
#     result_li.sort()
#     print(min(result_li))

# main()

# 模範解答
def collect_main():
    n,k = map(int, input().split())
    a = set(map(int, input().split()))
    
    for i in range(k):
        if i not in a:
            result = i
            break
    else:
        result = k
    print(result)

collect_main()