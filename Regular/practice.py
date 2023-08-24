string = input('Enter the string: ')
positive_sum = 0
negative_sum = 0
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
i = 0
while i < len(string):
	if string[i] == '-' and string[i+1].isdigit():
		temp_string = str()
		i += 1
		for j in string[i:]:
			if j.isdigit():
				temp_string += j
				i += 1
			else:
				break
		negative_sum -= int(temp_string)
		if int(temp_string) % 2 == 0:
			even_sum -= int(temp_string)
			even_count += 1
		else:
			odd_sum -= int(temp_string)
			odd_count += 1
	elif string[i].isdigit():
		temp_string = str()
		for j in string[i:]:
			if j.isdigit():
				temp_string += j
				i += 1
			else:
				break
		positive_sum += int(temp_string)
		if int(temp_string) % 2 == 0:
			even_sum += int(temp_string)
			even_count += 1
		else:
			odd_sum += int(temp_string)
			odd_count += 1
	else:
		i += 1
print(f'Positive sum: {positive_sum}\tNegative sum: {negative_sum}')
print(f'Even sum: {even_sum}\tOdd sum: {odd_sum}')
print(f'Even count: {even_count}\tOdd count: {odd_count}')
