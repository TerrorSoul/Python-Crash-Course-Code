class User():
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.login_attempts = 0
		
	def describe_user(self):
		print("The user's name is " + self.first_name + ' ' + self.last_name)
		
	def greet_user(self):
		print('Hello, ' + self.first_name + ' ' + self.last_name)
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
	
class Admin(User):
	def __init__(self, first_name, last_name, privileges):
		super().__init__(first_name, last_name)
		self.privileges = privileges
		
	def show_privileges(self):
		print(self.privileges)
	
user = Admin('Josiah', 'Carlson', 'can add post')
user.show_privileges()

