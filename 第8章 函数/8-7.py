def make_album(name, album, number):
	if number:
		return {'name': name, 'album': album, 'number': number}
	else:
		return {'name': name, 'album': album}

album = make_album('Jack', 'A', 5)
print(album)
album = make_album('Bob', 'B', 6)
print(album)
album = make_album('Frank', 'C', 7)
print(album)
