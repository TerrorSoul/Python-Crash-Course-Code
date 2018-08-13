like_nums = {'Josiah': [1, 6], 'Carlson': [2, 7], 'Aravind': [3, 6, 7], 'Shenoy': [4, 9], 'Ulrich': [5, 6]}
for key, value in like_nums.items():
	print(key + 'likes ')
	for num in value:
		print('\t' + str(num))
