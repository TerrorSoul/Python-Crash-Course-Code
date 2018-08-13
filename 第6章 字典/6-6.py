favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python',}
survery = ['jen', 'josiah', 'sarah', 'carlson', 'edward', 'aravind']
for name in survery:
	if name in favorite_languages.keys():
		print('Thank you for joining our survery')
	else:
		print('Would you want to join our survery')
