prompt = 'Enter a pizza ingredient:'
message = ''
message = input(prompt)
while message != 'quit':
	print('We will add ' + message + ' into the pizza')
	message = input(prompt)
