def quicksort(arr, low, high):
	if low < high:
		pivot = partation(arr, low, high)
		quicksort(arr, low, pivot - 1)
		quicksort(arr, pivot + 1, high)


def partation(arr, low, high):
	l, h = low, high
	pivot = arr[l]
	low = low + 1
	if l != h and l < h:
		while low <= high:
			if arr[high] < pivot < arr[low]:
				arr[high], arr[low] = arr[low], arr[high]
			if not arr[low] > pivot:
				low += 1
			if not arr[high] < pivot:
				high -= 1
	arr[l], arr[high] = arr[high], arr[l]
	return high


arr = [9, 8, 7, 6, 5, 11, 11, 11, 22, 22, 33, 33, 55, 55, 55, 66, 99, 44, 4, 3, 2, 1, 0]
quicksort(arr, 0, len(arr)-1)
print(arr)
