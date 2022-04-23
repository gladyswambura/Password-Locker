#!usr/bin/env python3.8
import unittest         # import unittest module
from user import User   # import User class from user.py

class Testuser(unittest.TestUser):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gladys","1234") # create user object with username and password as the arguments
    

