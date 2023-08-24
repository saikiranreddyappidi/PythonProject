from PP.general.Max import Max
from PP.general.pairs import pairs
from PP.general.tools import tools
from PP.general.weight import weight

N = int(input())
M = int(input())
m = Max(N, M)
print(m.Max_closest_number())
S = input()
s = weight(S)
print(s.getweight())
tools().reduce()
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs(arr).getpairs()
