def make_album(name, album):
	return {'name': name, 'album': album}

while True:
	print("Please tell me the album's information:")
	print("(enter 'q' at any time to quit)")
	
	name = input('name:')
	if name == 'q':
		break;
		
	album = input('album:')
	if album == 'q':
		break;
		
	album = make_album(name, album)
	print(album)
