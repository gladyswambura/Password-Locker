import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Arinah","Arinahgladoo","12345")   # create credentials object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []  #clearing the credentials list after each test case

# test case 1
    def test_init(self):                           
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.account_name,"Arinah")
        self.assertEqual(self.new_credentials.account_username,"Arinahgladoo")
        self.assertEqual(self.new_credentials.account_password,"12345")

# test case 2
    def test_save_credentials(self):  
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials()    #saving the credentials
        self.assertEqual(len(Credentials.credentials_list),1)     #checking if the length of the list is 1

# test case 3
    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credentials from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Arinah","Arinahgladoo","12345")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

# test case 4
    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials to our credentials list
        '''
        self.new_credentials.save_credentials()                    #saving the new credentials
        test_credentials = Credentials("Lorenah","Lola","6789@")   # new credentials
        test_credentials.save_credentials()                        #saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),2)   #checking if the length of the list is 2

# test case 5
    def test_confirm_credentials_exists(self):
        '''
        test_confirm_credentials_exists to check if we can return a Boolean 
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Lorenah","Lola","6789@")
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("Lorenah")    #confirming if the credentials exist
        self.assertTrue(credentials_exists)                              

# test case 6
    def test_display_all_credentials(self):
        '''
        test_display_all_credentials to test if we can display a list of all our credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)   #checking if the list is equal to the credentials_list
        ##copy and paste the credentials_list to the clipboard

if __name__ == '__main__':
    unittest.main()