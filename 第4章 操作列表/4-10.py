cube = [value**3 for value in range(1, 11)]
for value in cube:
	print(value)

print('The first three items in the list are ')
print(cube[:3])
print('Three items from the middle of the list are ')
print(cube[3:6])
print('The last three items in the list are ')
print(cube[-3:])
