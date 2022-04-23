class User:
    '''
    This class generates a new instance of user class
    '''

user_list=[] # users will be appended in this list

def __init__(self,user_name,password):
    '''
    Method to define the properties of each user object.
    '''
    self.user_name=user_name
    self.password=password

def save_user(self):
    '''
    save_user method saves user objects into user_list
    '''
    User.user_list.append(self)

def delete_user(self):
    '''
    delete_user method deletes a saved user from the user_list
    '''
    User.user_list.remove(self)

@classmethod
def find_by_first_name(cls,user_name, password):
    '''
    Method that takes in a username and returns a user that matches that username.
    '''
    user = ''
    for user in cls.user_list:
        if user.user_name == user_name and user.password == password:
            user=user.user_name
            return user


    