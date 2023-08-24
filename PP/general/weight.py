class weight:
	def __init__(self, s):
		self.s = s
	
	def getweight(self):
		alph = [chr(i) for i in range(97, 123)]
		res = 0
		for i in self.s:
			x = alph.index(i) + 1
			res = res + x
		return res
