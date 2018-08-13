import json

filename = 'favorite_number.json'

with open(filename, 'w') as file_object:
	number = input('Enter your favorite number:')
	json.dump(number, file_object)

with open(filename) as file_object:
	number = json.load(file_object)
	print('I know your favorite number! It is ' + number)
