#!/usr/bin/env python3.8
from user import User
from credentials import Credentials

# user
def create_user_account(user_name,password):
    '''
    Create a new user account
    '''
    new_user = User(user_name,password)
    return new_user


def verify_user(username, password):
    '''
    login  an existing user with the username and password
    '''
    verify_user = User.verify_user(username, password)
    return verify_user


def save_user(self):
    '''
    save user account
    '''
    User.user_list.append(self)         #Appends the new user to the user list


def find_by_username(username):
    '''
    Method that takes in an account name and returns a credentials that matches that account name.
    '''
    for user in User.users_list:
        if user.username == username:
            return user


def display_user():
    '''
    Display all the saved user accounts
    '''
    return User.display_user()


def delete_user(self):
    '''
    delete user
    '''
    User.user_list.remove(self) #removes the new user from the user list


#credentials
def create_new_credentials(account_name,Arinahgladoo,account_password):
    '''
    Create a new account
    '''
    new_credentials = Credentials(account_name, Arinahgladoo, account_password)
    return new_credentials


def save_credentials(self):
    '''
    save credentials
    '''
    Credentials.credentials_list.append(self)         #Appends the new credentials to the credentials list 


def delete_credentials(self):
    '''
    deletes existing credentials
    '''
    Credentials.credentials_list.remove(self)         #removes the new credentials from the credentials list


def find_account(account_name):
    '''
    Method that takes in an account name and returns a credentials that matches that account name.
    '''
    for credentials in Credentials.credentials_list:
        if credentials.account_name == account_name:
            return credentials

def verify_credentials(self):
    '''
    Method that checks if the account name exists in the credentials_list.
    '''
    for credentials in Credentials.credentials_list:
        if credentials.account_name == self.account_name:   #if the account name matches the account name in the credentials list
           return True
        return False


def display_Credentials():
    '''
    Display all the saved credentials
    '''
    return display_Credentials()      #returns the credentials list 


def generate_password(self):
    '''
    generate password randomly
    '''
    gen_password=Credentials.generate_password(self)
    return gen_password


def main():                        #this function is responsible for the flow of the application
    print("Hello, welcome to password locker!")
    print('\n')
    print("To login to your account, enter shortcode 'l' To sign up, enter shortcode 's' to to exit the program enter short code 'e'")
    print('\n')

    while True:                     #this is the main loop, it will keep running until the user enters the short code 'e'
        short_code=input().lower()  #The user input is converted to lowercase
       
        if short_code=="s":        #create account
            print("Enter your name to start signing up")
            name = input ()
            print(f"{name}, Sign up to start")
            print("-"*60)
            print('To create a new account, Enter your account_name')
            account_name=input()
            print('Enter a password')
            account_password=str(input())
            save_user(create_user_account(account_name, account_password))
            print(f"Account name:{account_name} \n Password:{account_password}")
            print('Write a username, one that you can remember')
            username=input()
            print(f"Hello {username}, your account has been successfully created!")
            print("*"*60)       #prints a line of stars
            print(f"To create a new account, enter:\n 'na'for a new account,\n  'ex'for an existing account \n")
        
        while True:
            print("To proceed select any:\n CC - Create a new credential  \n DS-Display your credentials \n FC - Find a credential \n D - Delete credential \n EX - Exit the application \n") 
            short_code = input().lower().strip()
            print("*"*70)


        if short_code=="l":          #login
            print("-"*60)            #prints a line of dashes
            print('To login, Enter your username')
            username=input().strip
            print('Enter your password')
            password=str(input()).strip
            user_exists=verify_user(username, password)
            if  user_exists == username:
                print(f"Welcome {username}!!, you are now logged in")
            elif user_exists !=username:
                print("Wrong username, use shortcode 'c' to create an account")
            elif user_exists !=password:
                print("Invalid password!, use shortcode 'c' to create an account")
                print("*"*60)
          


        elif short_code == "e":
            print("-"*60)
            print("Thank you for using password locker")
            break  




if __name__ == '__main__':
    main()