current_users = ['Josiah', 'John', 'Carlson', 'Thomas', 'Cormen']
new_users = ['Charles', 'Leiserson', 'John', 'Ronald', 'Rivest']
for new_user in new_users:
	if new_user in current_users:
		print('Enter another name')
	else:
		print('The name have not been used')
