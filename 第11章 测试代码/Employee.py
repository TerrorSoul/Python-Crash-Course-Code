class Employee():
	def __init__(self, first_name, last_name, raises):
		self.first_name = first_name
		self.last_name = last_name
		self.raises = raises
	def give_raise(self, upraise=5000):
		self.raises += upraise
