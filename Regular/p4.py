from itertools import permutations

arr=input()
comb=list(permutations(arr,len(arr)))
print(comb)