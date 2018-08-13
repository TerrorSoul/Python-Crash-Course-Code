prompt = 'Enter your age:'
age = ''
age = input(prompt)
while age != 'quit' and age != '':
	age = int(age)
	if age < 3:
		print('You are free')
	elif age < 12:
		print('Your price is 10 dollars')
	else:
		print('Your price is 15 dollars')
	age = input(prompt)
