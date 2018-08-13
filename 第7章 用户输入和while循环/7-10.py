prompt = 'If you could visit one place in the world, where would you go?'
place = input(prompt)
places = []
while place != 'quit' and place != '':
	places.append(place)
	place = input(prompt)

print('The palces you want to visit are:')
for place in places:
	print('\t' + place)
