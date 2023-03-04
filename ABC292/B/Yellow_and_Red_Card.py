# AC
def main():
    N, Q = map(int, input().split())
    E_count = [0]*N
    for i in range(Q):
        e_1, e_2 = map(int, input().split())
        if e_1==1:
            E_count[e_2-1] += 1
        elif e_1==2:
            E_count[e_2-1] += 2
        elif e_1==3:
            if E_count[e_2-1]>=2:
                print('Yes')
            else:
                print('No')
    

main()