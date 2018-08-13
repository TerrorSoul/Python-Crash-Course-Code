def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	m = []
	for magician in magicians:
		magic = 'the Great ' + magician
		m.append(magic)
	return m
		
magicians = ['Jack', 'Bob', 'Frank']
m = make_great(magicians)
show_magicians(magicians)
show_magicians(m)
