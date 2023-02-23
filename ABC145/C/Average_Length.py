# AC
import math
import itertools

N = int(input())
x = [list(map(int, input().split())) for i in range(N)]
n_fanctorial = math.factorial(N)
x_pers = list(itertools.permutations(x, N))

l = 0
for x_per in x_pers:
    for j in range(N-1):
        l += math.sqrt((x_per[j][0]-x_per[j+1][0])**2+(x_per[j][1]-x_per[j+1][1])**2)
print(l/n_fanctorial)