from itertools import combinations

arr=input()
comb=list(combinations(arr,len(arr)-1))
print(comb)