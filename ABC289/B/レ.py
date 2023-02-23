# AC
def main():
    N, M = map(int, input().split())
    a_l = list(map(int, input().split()))
    all_l = [i for i in range(1,N+1)]
    n_l = list(set(all_l)-set(a_l))
    n_l.sort()
    result_l = []
    for i in n_l:
        result_l += [j for j in range(i, 0, -1)]
    print(' '.join(map(str, sorted(set(result_l), key=result_l.index))))

main()

# こういう風に解いてる人もいた
# A, B = map(int, input().split())
# l = list(map(int, input().split()))
# ans=[]
# karilist=[]
 
# for i in range(1,A+1):
#   a = i in l
#   if a:
#     karilist.insert(0,i)
#   else:
#     ans.append(i)
#     ans.extend(karilist)
#     karilist.clear()
    
# print(*ans)
