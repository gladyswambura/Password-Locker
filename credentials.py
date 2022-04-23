import random
import string


class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = [] # credentials will be appended in this list

    def __init__(self,account_name,account_username,account_password):
        '''
        Method to define the properties of each credentials object.
        '''
        self.account_name = account_name
        self.account_username = account_username
        self.account_password = account_password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)     

    def generate_password(self):
        '''
        generate_password method generates a random password for the user
        '''
        password= string.ascii_uppercase + string.ascii_lowercase+string.digits
        return ''.join(random.choice(password) for i in range(8))

    @classmethod
    def verify_credentials(cls,account_name):
        '''
        Method that checks if the account name exists in the credentials_list.
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
            return False

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in an account name and returns a credentials that matches that account name.
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials
