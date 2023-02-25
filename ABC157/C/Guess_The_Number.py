# AC 
# コメント：ifが多くて汚い。もっと問題の条件を整理して考えないとWAばっかでる。
def main():
    N, M = map(int, input().split())
    L = {}
    if M==0:
        if N==1:
            print(0)
            return
        if N==2:
            print(10)
            return
        if N==3:
            print(100)
            return
    for i in range(M):
        s, c = map(int, input().split())
        if (s in L)and(L[s]!=c):
            print(-1)
            return
        else:
            L[s] = c
    for i in range(1,N+1):
        if (i not in L):
            if i==1:
                L[i] = 1
            else:
                L[i] = 0
    L = dict(sorted(L.items(), reverse=False))
    if (len(L)!=1)and(L[1] == 0):
        print(-1)
        return
    result = ''
    for k, v in L.items():
        result+=str(v)
    print(int(result))


main()

# 模範１(全探索)
# n, m = map(int, input().split())
# sc_li = [list(map(int,input().split())) for _ in range(m)]
# sc = []
# ans = ""

# for i in range(1000):
#     flag = True
#     ans = str(i)
#     if len(ans) != n:
#         continue
#     for j in range(m):
#         si, ci = sc_li[j]
#         if int(ans[si-1]) != ci:
#             flag = False
#     if flag:
#         print(ans)
#         exit(0)

# print(-1)

# 模範2
# n, m = map(int, input().split())

# li = [0] * n

# for i in range(m):
#     si, ci = map(int, input().split())
#     if li[si-1] != 0 and li[si-1] != ci:
#         print(-1)
#         exit(0)
#     if si == 1 and ci == 0:
#         if n > 1:
#             print(-1)
#             exit(0)
#     li[si-1] = ci

# if n > 1 and li[0] == 0:
#     li[0] = 1

# for i in range(n):
#     print(li[i], end="")