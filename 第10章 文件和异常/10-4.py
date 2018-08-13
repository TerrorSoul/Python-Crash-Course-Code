with open('guest_book.txt', 'a') as file_object:
	while True:
		name = input('Enter your name:')
		if name == 'q':
			break
		print('Hello, ' + name)
		file_object.write(name + '\n')
	
