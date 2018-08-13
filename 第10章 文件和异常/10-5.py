with open('program_reason.txt', 'a') as file_object:
	while True:
		reason = input('Enter your reason for loving programming:')
		if reason == 'q':
			break
		file_object.write(reason + '\n')
	
