class Max:
	def __init__(self, N, M):
		self.N = N
		self.M = M
		
	
	def Max_closest_number(self):
		m = 10 ** 5
		for i in range(-2 * self.N, 2 * self.N):
			x = abs(i - self.N)
			if x < m and i % self.M == 0:
				m = x
				val = i
			elif x == m and val < i and i % self.M == 0:
				val = i
		return val
	
	
