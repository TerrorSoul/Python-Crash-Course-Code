pets = {'huang': {'type': 'dog', 'owner': 'Aravind'}, 'hua': {'type': 'cat', 'owner': 'Shenoy'}}
for key, value in pets.items():
	print(key + ' is a ' + value['type'] + ', its owner is ' + value['owner'])
