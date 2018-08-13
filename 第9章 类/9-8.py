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

class Privileges():
	def __init__(self):
		self.privileges = 'can add post'
		
	def show_privileges(self):
		print(self.privileges)
	
class Admin(User):
	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = Privileges()
	
user = Admin('Josiah', 'Carlson')
user.privileges.show_privileges()

