while True:
	try:
		num1 = input('Enter a number:')
		if num1 == 'q':
			break
		num1 = int(num1)
		num2 = input('Enter another number:')
		if num2 == 'q':
			break
		num2 = int(num2)
	except ValueError:
		print('You should enter two numbers')
	else:
		print(num1 + num2)
