sandwich_orders = ['tuna sandwich', 'chick sandwich', 'soft sandwich']
finished_sanwich = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich)
	finished_sanwich.append(sandwich)

print(finished_sanwich)
