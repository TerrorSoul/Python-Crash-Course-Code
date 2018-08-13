cities = {'New York': {'country': 'USA', 'population': '100000', 'fact': 'big city'},
'Chicago': {'country': 'USA', 'population': '105500', 'fact': 'interesting city'},
'San Francisco': {'country': 'USA', 'population': '652300', 'fact': 'maybe a rich city'}}
for city, info in cities.items():
	print(city + ': ')
	for key, value in info.items():
		print('\t' + key + ': ' + value)
