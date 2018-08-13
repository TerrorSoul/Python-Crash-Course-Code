information1 = {'first_name': 'Josiah', 'last_name': 'Carlson', 'age': 37, 'city': 'New York'}
information2 = {'first_name': 'Aravind', 'last_name': 'Shenoy', 'age': 28, 'city': 'Chicago'}
information3 = {'first_name': 'Ulrich', 'last_name': 'Sossou', 'age': 39, 'city': 'San Francisco'}
people = [information1, information2, information3]
for information in people:
	print(information['first_name'] + ' ' + information['last_name'] + ' is ' + str(information['age'])
+ ' years old, he lives in ' + information['city'])
