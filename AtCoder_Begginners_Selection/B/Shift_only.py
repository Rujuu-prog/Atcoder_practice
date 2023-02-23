#AC
#再帰関数ではなくwhileで実装した方が良いかも
def d(N, a_l, num:int):
    a_l = [i/2 for i in a_l if i%2==0]
    if len(a_l) == N:
        num += 1
        d(N, a_l, num)
    else:
        print(num)


def main():
    N = int(input())
    a_l = [int(i) for i in input().split()]
    num = 0
    d(N, a_l, num)

main()

# 模範解答(https://kihor.com/kp_py_atc_abc081b/)
# n = input()
# a = list(map(int, input().split()))
# cnt = 0
# while all(i%2==0 for i in a):
#     a = [i/2 for i in a]
#     cnt += 1
# print(cnt)