import threading
import time


def print_even(num):
	for i in range(0, num):
		if i % 2 == 0:
			print("Even: {}" .format(i))

def print_odd(num):
	for i in range(0, num):
		if i % 2 != 0:
			print("Odd: {}" .format(i))

if __name__ =="__main__":
	num = int(input("Enter a number: "))
	t1 = threading.Thread(target=print_even(num), args=(10,))
	t2 = threading.Thread(target=print_odd(num), args=(10,))
	t1.start()
	t2.start()
	t0=time.time()
	t1.join()
	t2.join()
	t1=time.time()
	print("Time taken: {}" .format(t1-t0))
	print("Done!")
