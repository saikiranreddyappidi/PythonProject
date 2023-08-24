import time


def open_File():
	f = open("performanceTesting.txt", "r")
	for i in f.readlines():
		print(i)
	f.close()
	return


def line_count():
	f = open("performanceTesting.txt", "r")
	print("Line count", len(f.readlines()))
	f.close()
	return


def copying():
	src = open("performanceTesting.txt", "r")
	desti = open("copiedfile.txt", "a")
	i = src.readlines()
	desti.writelines(i)
	src.close()
	desti.close()
	print("Files copied")
	return


def space_cnt():
	f = open("performanceTesting.txt", "r")
	line = f.read()
	print("Space count", line.count(" "))
	f.close()
	return


def increase_lines():
	f = open("performanceTesting.txt", "r")
	line = f.readlines()
	f.close()
	f = open("performanceTesting.txt", "a")
	f.writelines(line)
	f.close()
	print("Line increased in the file")


t = 1
while t:
	begin = time.time()
	open_File()
	end = time.time()
	print("Time taken to open a file: ", end - begin)
	begin = time.time()
	line_count()
	end = time.time()
	print("Time taken to count the lines: ", end - begin)
	begin = time.time()
	copying()
	print("Time taken to copy the contents of the file to another file is: ", end - begin)
	begin = time.time()
	space_cnt()
	end = time.time()
	print("Time to count no.of spaces in the file are: ", end - begin)
	begin = time.time()
	end = time.time()
	print("Time taken to increase a line is: ", end - begin)
	t -= 1
