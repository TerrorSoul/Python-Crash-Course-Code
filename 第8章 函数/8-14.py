def make_car(maker, model, **information):
	profile = {}
	profile[maker] = maker
	profile[model] = model
	for key, value in information.items():
		profile[key] = value
		
	print(profile)
	
make_car('subaru', 'outback', color='blue', tow_package=True)
