# AC len(C)じゃなくてNを使っても良かったかも

def main():
    N = int(input())
    S = input()
    X = 0
    Y = 0
    C = ['0:0']
    for s in S:
        if s=='R':
            X+=1
        elif s=='L':
            X-=1
        elif s=='U':
            Y+=1
        elif s=='D':
            Y-=1
        C.append(str(X)+':'+str(Y))
    if len(C) != len(set(C)):
        print('Yes')
    else:
        print('No')

main()