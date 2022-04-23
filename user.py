class User:
    '''
    This class generates a new instance of user class
    '''

user_list=[] # users will be appended in this list

def __init__(self,first_name,last_name,password):
    '''
    Method to define the properties of each user object.
    '''
    self.first_name=first_name
    self.last_name=last_name
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

