try:
	num1 = input('Enter a number:')
	num1 = int(num1)
	num2 = input('Enter another number:')
	num2 = int(num2)
except ValueError:
	print('You should enter two numbers')
else:
	print(num1 + num2)
