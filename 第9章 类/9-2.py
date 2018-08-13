class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.restaurant_name)
		print("The restaurant's cuisine is " + self.cuisine_type)
		
	def open_restaurant(self):
		print('The restaurant is open')
		
restaurant1 = Restaurant('Wonder', 'Hot')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('Beauty', 'Soft')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('Wooden', 'Brow')
restaurant3.describe_restaurant()
