"""Six friends went to Goa and are looking for accommodation for three days. After approaching a broker he suggested
them  a hotel which offers two types of rooms — double rooms and triple rooms. A double room costs Rs. X,
while a triple room costs Rs. Y. The friends can either get three double rooms or get two triple rooms. Find the
minimum amount they will have to pay to accommodate all six of them. """

x, y = map(int, input("Enter the price of double and triple rooms: ").split())
print("Minimum amount: ", min(3 * x, 2 * y))
if 3 * x > 2 * y:
	print("Better to get 2 triple rooms")
elif 3 * x < 2 * y:
	print("Better to get 3 double rooms")
else:
	print("Either is good")
