arr = [5, 9, 6, 4, 2, 3, 8, 7, 1]
n = len(arr)
for i in range(n):
	swap = False
	for j in range(n - i - 1):
		if arr[j] > arr[j + 1]:
			arr[j], arr[j + 1] = arr[j + 1], arr[j]
			swap = True
	if not swap:
		break
print(arr)
