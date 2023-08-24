import os

seperator = '''----------------------------------------------------------------\n'''
file_menu = seperator + '''0.Exit\n1.Open a file\n2.Copy content of the file\n3.Replace a word in the file
4.Get no.of lines in the file\n5.Get space count of the file'''
directory_menu = seperator + '''0.Exit\n1.Navigate to another Directory\n2.Remove specified Directory
Note:We can remove or navigate to a specified directory only if it exits and doesn't require any permissions. '''


def getinput():
	flag = True
	while flag:
		try:
			choice = int(input("Enter your choice: "))
			return choice
		except ValueError:
			flag = True
			print("Enter a valid choice in Integer format(1,2,..,5)")
		except SyntaxError:
			flag = True
			print("Enter only one value in integer format")


def getfile(filename, mode):
	try:
		f = open(filename, mode)
		return f
	except UnicodeDecodeError:
		print("We can't open such file: ", filename)
	except FileNotFoundError:
		print("File not found in this directory: ", filename)
	except PermissionError:
		print("Permission error occurred when opening the file: ", filename)
	except:
		print("Undefined Error occurred")
	return 0


def copyfile(src, dest):
	resource = getfile(src, "r")
	target = getfile(dest, "a")
	if not resource and target:
		return
	for i in resource.readlines():
		target.writelines(i)
	print("Content copied successfully.")
	resource.close()
	target.close()
	return


def getlist():
	print("Available files are:")
	arr = os.listdir(os.getcwd())
	for i, j in zip([_ for _ in range(len(arr))], arr):
		print(i, j, sep=". ")
	return arr


def readfile(filename):
	f = getfile(filename, "r")
	if not f:
		return
	try:
		print(f.read())
	except UnicodeDecodeError:
		print("We can't read the file in this format: ", filename)
	f.close()
	return


def update(word, replace, filename):
	arr = []
	f = open(filename, "r")
	lines = f.readlines()
	f.close()
	for i in lines:
		if word in i:
			i = i.replace(word, replace)
			print("Replaced successfully.")
		arr.append(i)
	f = open(filename, "w")
	for i in arr:
		f.writelines(i)
	f.close()
	return


def files():
	try:
		print(file_menu)
		choice = getinput()
		if choice == 0:
			return
		elif choice == 1:
			readfile(getlist()[getinput()])
		elif choice == 2:
			arr = getlist()
			src, dest = map(int, input("Enter two values to copy the contents(1->2):").split())
			copyfile(arr[src], arr[dest])
		elif choice == 3:
			filename = getlist()[getinput()]
			print("The contents of the file are: ")
			readfile(filename)
			here, replace = map(str, input("Enter the word to be replaced and to replace with").split())
			update(here, replace, filename)
		elif choice == 4:
			filename = getlist()[getinput()]
			f = getfile(filename, "r")
			if not f:
				files()
			line = f.readlines()
			f.close()
			print("No.of lines in the file are: ", len(line))
		elif choice == 5:
			filename = getlist()[getinput()]
			f = getfile(filename, "r")
			if not f:
				files()
			line = f.read()
			print("No.of spaces: ", line.count(" "))
			f.close()
		else:
			print("Enter a valid choice.")
		files()
	except IndexError:
		print("Index list out of range error.Please enter the input within the range.")
		files()
		

def directory():
	print(directory_menu)
	choice = getinput()
	if choice == 0:
		return
	elif choice == 1:
		path = input("Enter the path: ")
		try:
			os.chdir(path)
			print("The path current working directory changed to: ", os.getcwd())
		except:
			print("An error occurred when navigating to :", path)
	elif choice == 2:
		path = input("Enter the path: ")
		try:
			os.remove(path)
			print(path, " :Path removed successfully.")
		except:
			print("An error occurred when removing the path: ", path)
	else:
		print("Enter a valid input")
	directory()


def main():
	print("Current working directory: ", os.getcwd())
	print("0.Exit", "1.Files menu", "2.Directory menu", sep="\n")
	choice = getinput()
	if choice == 0:
		exit(3)
	elif choice == 1:
		files()
		print(seperator)
	elif choice == 2:
		directory()
		print(seperator)
	else:
		print("Enter a valid choice")
	print(seperator)
	main()


if __name__ == '__main__':
	main()
