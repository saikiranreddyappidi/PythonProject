class pairs:
	def __init__(self, arr):
		self.arr = arr
	
	def getpairs(self):
		for i in range(len(self.arr) - 1):
			text = '({},{})'.format(self.arr[i], self.arr[i + 1])
			print(text, end=",")