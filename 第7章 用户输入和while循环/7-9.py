sandwich_orders = ['tuna sandwich', 'pastrami', 'chick sandwich', 'pastrami', 'soft sandwich']
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

finished_sanwich = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich)
	finished_sanwich.append(sandwich)

print(finished_sanwich)
