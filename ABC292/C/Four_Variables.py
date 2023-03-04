# WA
import itertools

def main():
    N = int(input())
    L = [i for i in range(1, N)]
    c = 0
    L_ini = []
    for p_1 in itertools.combinations_with_replacement(L, 2):
        cal = p_1[0]*p_1[1]
        if cal > N:
            print(cal)
            break
        L_ini.append(cal)
    print(L_ini)
    for p_2 in itertools.combinations_with_replacement(L_ini, 2):
        if p_2[0]+p_2[1] == N:
            c+=1
    print(c)
    print(c*4)

main()
