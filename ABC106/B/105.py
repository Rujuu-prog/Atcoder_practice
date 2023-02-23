#TODO:AC 全探索例
def cal(l):
    num = 0
    for i in range(1,l+1):
        if l%i == 0:
            num+=1
    if num==8:
        return 1
    else:
        return 0
    

def main():
    N = int(input())
    L = [i for i in range(1, N+1) if i%2!=0]
    result = 0
    for l in L:
        cal_re = cal(l)
        result += cal_re
    print(result)

main()