#!usr/bin/env python3.8
import unittest         # import unittest module
from user import User   # import User class from user.py

class Testuser(unittest.TestUser):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):   # setUp method to create an instance of user before each test case
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Gladys","1234") # create user object with username and password as the arguments

    def tearDown(self):   # tearDown method to clean up after each test case has run
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

# First test case
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"Gladys")
        self.assertEqual(self.new_user.password,"1234")

# Second test case
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_user()               # saving the new user
        self.assertEqual(len(User.user_list),1) # self.assertEqual is used to check if the list is not empty
        
# Third test case
    
    


