# AC
def main():
    N = int(input())
    ai = list(map(int, input().split()))
    ai_sorted = sorted(ai, reverse=True)
    alice = 0
    bob = 0
    for index, num in enumerate(ai_sorted):
        if index%2==0:
            alice+=num
        else:
            bob+=num
    print(alice-bob)

main()

# 模範解答
# # input関数をint関数で囲み、整数値として変数Nに設定
# N = int(input())
# # input().split()で空白区切りの文字列を取得 → intに変換 → list関数で囲み、リストとしてaに設定
# a = list(map(int, input().split()))
# # sortメソッドの引数にreverse=Trueを設定し、リストを降順に並べ替える
# a.sort(reverse=True)
# # スライスを[0::2]と設定し、リストの偶数番目を取得
# Alice_calds = a[0::2]
# # スライスを[1::2]と設定し、リストの奇数番目を取得
# Bob_calds = a[1::2]
# # sum関数でそれぞれの合計値を求め、Aliceの合計値からBobの合計値を引く
# ans = sum(Alice_calds)-sum(Bob_calds)
# # print関数で結果を表示
# print(ans)