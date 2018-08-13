try:
	with open('cats.txt') as file_object:
		print('cats:')
		for line in file_object:
			print('\t' + line.rstrip())
	with open('dogs.txt') as file_object:
		print('dogs:')
		for line in file_object:
			print('\t' + line.rstrip())
except FileNotFoundError:
	pass
