import unittest
from Employee import Employee

class test(unittest.TestCase):
	def setUp(self):
		self.employee = Employee('Josiah', 'Carlson', 2000)
		
	def test_give_default_raise(self):
		self.employee.give_raise()
		raises = self.employee.raises
		self.assertEqual(raises, 7000)
		
	def test_give_custom_raise(self):
		self.employee.give_raise(3000)
		raises = self.employee.raises
		self.assertEqual(raises, 5000)

unittest.main()
