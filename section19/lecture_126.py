



import unittest

from test_function_1 import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""Tests for the 'name_function.py."""
	
	def test_first_last_name(self):
		"""Do name with middle names work?"""
		formatted_name = get_formatted_name('tony', 'staunton')
		self.assertEqual(formatted_name, 'Tony Staunton')
		
unittest.main()

	