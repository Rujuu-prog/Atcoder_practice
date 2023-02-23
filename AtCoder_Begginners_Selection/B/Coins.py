#AC
#模範解答
def main():
    A_500 = int(input())
    B_100 = int(input())
    C_50 = int(input())
    X = int(input())
    count = 0
    for i in range(A_500+1):
        for j in range(B_100+1):
            for k in range(C_50+1):
                if 500*i+100*j+50*k == X:
                    count += 1
    print(count)
main()