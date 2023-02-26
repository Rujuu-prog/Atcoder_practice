# DPで解くらしい。メモ化再帰でも？

# import itertools

# def Check(A,B,P,N):
#     result=0
#     A_c = A[:]
#     B_c = B[:]
#     F_n = []
#     F = []
#     for p in P:
#         A_c[p], B_c[p] = B_c[p], A_c[p]
#         F_n.append(p)
#         F_n.append(p+1)
#         F_n.append(p-1)
#     F_n = list([i for i in set(F_n) if (i >= 0)and(i<N)])
#     for f_n in F_n:
#         F.append(A_c[f_n])
#     print(F)
#     if len(F) == len(set(F)):
#         print('ok')
#         result += 1
#     return result

# def main():
#     N = int(input())
#     A = []
#     B = []
#     result = 0
#     for i in range(N):
#         a, b = map(int, input().split())
#         A.append(a)
#         B.append(b)
#     if len(A) == len(set(A)):
#         result += 1
#     S = [i for i in range(N)]
#     for s in S:
#         A_c = A[:]
#         B_c = B[:]
#         F_n = []
#         F = []
#         A_c[s], B_c[s] = B_c[s], A_c[s]
#         F_n.append(s)
#         F_n.append(s+1)
#         F_n.append(s-1)
#         F_n = list([i for i in set(F_n) if (i >= 0)and(i<N)])
#         for f_n in F_n:
#             F.append(A_c[f_n])
#         print(F)
#         if len(F) == len(set(F)):
#             print('ok')
#             result += 1
#     for i in range(1, N+1):
#         print('i:',i)
#         for P in itertools.combinations(S, i):
#             result+=Check(A,B,P,N)
#     print(result)


# main()

import sys
input = sys.stdin.readline
 
n = int(input())
a = [0] * n
b = [0] * n
 
for i in range(n):
    x, y = map(int, input().split())
    a[i] = x
    b[i] = y
 
dp = [[0, 0] for i in range(n)]
dp[0][0] = 1
dp[0][1] = 1
 
mod = 998244353
for i in range(1, n):
    if a[i] != a[i - 1]:
        dp[i][0] += dp[i - 1][0]
    if a[i] != b[i - 1]:
        dp[i][0] += dp[i - 1][1]
    if b[i] != a[i - 1]:
        dp[i][1] += dp[i - 1][0]
    if b[i] != b[i - 1]:
        dp[i][1] += dp[i - 1][1]
 
    dp[i][0] %= mod
    dp[i][1] %= mod
 
print((dp[n - 1][0] + dp[n - 1][1]) % mod)