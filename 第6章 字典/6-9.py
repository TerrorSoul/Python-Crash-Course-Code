favorite_places = {'Aravind': ['New York', 'Beijing'], 'Shenoy': ['San Francisco', 'Hong Kong'], 'Ulrich': ['Chicago', 'Shanghai']}
for key, value in favorite_places.items():
	print(key + 'likes ')
	for city in value:
		print('\t' + city)
