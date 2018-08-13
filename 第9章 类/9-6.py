class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	
	def describe_restaurant(self):
		print("The restaurant's name is " + self.restaurant_name)
		print("The restaurant's cuisine is " + self.cuisine_type)
		
	def open_restaurant(self):
		print('The restaurant is open')
		
	def set_number_served(self, number):
		self.number_served = number
		
	def increment_number_served(self, number):
		self.number_served += number
		
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['salt', 'sweet', 'sour']
		
	def show_flavors(self):
		for flavor in self.flavors:
			print(flavor)
			
iceCreamStand = IceCreamStand('Frank', 'iceCream')
iceCreamStand.show_flavors()
