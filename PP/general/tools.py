import itertools


class tools:
	def __init__(self):
		pass
	
	def reduce(self):
		example = itertools.compress('ABCDE', [1, 0, 1, 1, 0])
		for each in example:
			print(each, end="")
			