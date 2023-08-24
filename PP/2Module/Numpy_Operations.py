import numpy

menu = '''0.Exit\n1.Get randomly generated array\n2.Get last two row values
3.Get sum of second row values\n4.Get maximum value with indexes
5.Add a new row\n6.Replace a specific value
7.Get how many values are less than given value\n8.Reshape the array to all possible shapes
9.Convert array datatype into float(float64)\n10.Get unique values in the array '''

arr = numpy.random.randint(10, 30, (5, 4))
flag = True
while flag:
	# print("Current array:", arr, sep="\n")
	print(menu)
	try:
		choice = int(input())
		if choice == 0:
			flag = False
		elif choice == 1:
			print(arr)
		elif choice == 2:
			print("Last row: ", arr[-1], "\nLast but one row: ", arr[-2])
		elif choice == 3:
			print("Sum of 2nd row values: ", sum(arr[3]))
		elif choice == 4:
			maxi = numpy.where(arr == numpy.amax(arr))
			print("Maximum number is: ", numpy.amax(arr))
			print("They are at: ")
			print(*list(zip(maxi[0], maxi[1])), sep="\n")
		elif choice == 5:
			last = numpy.array(numpy.random.randint(0, 10, (1, 4)))
			print("This the randomly generated row", last)
			arr = numpy.append([arr], [[last]]).reshape(6, 4)
			print(arr)
		elif choice == 6:
			x, z = map(int, input("Enter a value to replace and replace with: ").split())
			arr[x == arr] = z
			print(arr)
		elif choice == 7:
			x = int(input("Enter the x value: "))
			print("The no.of values less than", x, "are: ", arr[x > arr].size)
		elif choice == 8:
			s = arr.size
			print("All possible shapes of the array are: ")
			con = "Shape ({},{}):\n"
			for i in range(1, s):
				if s % i == 0:
					print(con.format(i, int(s / i)), arr.reshape(i, int(s / i)))
		elif choice == 9:
			arr = arr.astype("float64")
			print("After changing the datatype to float: \n", arr)
		elif choice == 10:
			print("Unique elements in the given array are: ", numpy.unique(arr))
		elif flag:
			print("Enter a valid choice")
	except:
		print("Enter a valid input.")
if not flag:
	exit(2)