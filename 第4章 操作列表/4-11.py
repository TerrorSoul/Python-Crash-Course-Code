pizza = ['New York Style', 'Chicago Style', 'California Style']
friend_pizzas = pizza[:]
pizza.append('Thick style')
friend_pizzas.append('Cracker and Thin Style')
print('My favorite pizzas are:')
for p in pizza:
	print(p)
	
print("My friend's favorite pizzas are:")
for p in friend_pizzas:
	print(p)
