def name(x, y):
	x1 = ''
	y1 = ''
	for i in range(len(x)):
		if i == 0:
			if 'a' <= x[i] <= 'z':
				x1 += chr(ord(x[i]) - 32)
			else:
				x1 += x[i]
		elif 'A' <= x[i] <= 'Z':
			x1 += chr(ord(x[i]) + 32)
		else:
			x1 += x[i]
	for i in y:
		if 'a' <= i <= 'z':
			y1 += chr(ord(i) - 32)
		else:
			y1 += i
	print(x1, y1)


def getinput():
	flag = True
	while flag:
		try:
			n1 = input("Enter the string :")
			print(n1)
			if " " not in n1:
				raise ValueError
			for i in n1:
				if (not ('a' <= i <= 'z') or ('A' <= i <= 'Z')) and i != " ":
					raise TypeError
			flag = False
		except TypeError:
			flag = True
			print("Enter correct type.Only english alphabets are allowed!!!")
		except ValueError:
			flag = True
			print("You need to enter two strings(firstname lastname)!!!")
	return n1


def main():
	names = getinput()
	print(names)
	fname, lname = map(str, names.split(" "))
	name(fname, lname)


main()
