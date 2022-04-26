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


def display_credentials():
    '''
    Display all the saved credentials
    '''
    return Credentials.display_credentials()       #returns the credentials list 


def generate_password(self):
    '''
    generate password randomly
    '''
    gen_password=Credentials.generate_password(self)
    return gen_password

def main():
    print("Welcome to password locker!")
    print("Enter your name to start signing up")
    name = input ()
    print(f"{name}, Sign up to start")
    print('\n')
    print("Reply with  : cc - Sign Up,  ex -exit ")
    print("-" * 80)
    while True:

        short_code = input().lower()
        if short_code == 'cc':
            print("Account creating process begins...")
            print("Please enter the following information:")
            print("Username: ")
            username = input()
            print("Password: ")
            password = input()
            save_user(create_user_account(username, password))
            print('\n')
            print(f"{name}'s Account information: ")
            print(f"Username: {username} , Password:{password}")
            print('\n')
            print(f"Logged in. Welcome {username}!")
            print("*" * 80)
            print("create new account, use:\n na--new account,\n  ex--existing account,\n")




            short_code = input("").lower().strip()

        if short_code=='na':
            print("Create new account i.e Facebook")
            print("Account name")
            account_name=input()
            print("username")
            username=input()
            print("password")
            password=""
            while True:
                print("Tp-type your password,\n Gp-generate password")
                pass_choice = input().lower().strip()
                if pass_choice=='tp':
                    print("\n")
                    
                    password=input("Enter password\n")
                    break

                elif pass_choice =='gp':
                    password = input(generate_password(password))
                    
                    break
                else:
                    print("Invalid password")

            save_user(create_user_account(username,password))
            print("-"*90)
            print(f"Hello {username}, Your {account_name} account  has been created succesfully created! Your password is: {password}")
            print("-"*90) 
        while True:


            print("To proceed select any:\n CC - Create a new credential  \n DS-Display your credentials \n FC - Find a credential \n D - Delete credential \n EX - Exit the application \n") 
            short_code = input().lower().strip()
            if short_code == "cc":
                print("Create new credentials")
                print("-"*80)
                print("Account name ....")
                account_name = input().lower()
                print("Your Account username")
                username = input()
                # while True:
                print(" TY - Type your own pasword if you already have an account:\n GR - Generate a random Password")
                password_Choice = input().lower().strip()
                if password_Choice=="ty":
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice=="GP":
                    password = generate_password(password)
                    break
                else:
                    print("invalid password")
                save_credentials(create_new_credentials(account_name,username,password))
                print('\n')
                print(f"Account Credential for:Account {account_name} :Username: {username} - Password:{password} created succesfully")
                print('\n')        
            if  short_code =="ds":
                print("ACCOUNT DETAILS ARE:")
                print(" "*30)

                for credential in display_credentials():
                    print(f"{credential.account_name}\n {credential.username}\n {credential.password}")
                else:

                    print("NO ACCOUNT!!!!")


            elif short_code=="fc":
                print("Which Account are you trying to find???")
                search_credentials= input()
                if find_account(search_credentials):
                    search_account=find_account(search_credentials)
                    print(f"{search_account.account_name}\n{search_account.username} \n {search_account.password}")
                else:
                    print("Account doesn't exist")
                    print('\n')


            elif short_code == "d":
                print("Enter account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_account(search_name):
                search_credential = find_account(search_name)
                print("_"*40)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account_name} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")   



            if short_code == "ex":
                print("Bye ....")
                break
            else:
                print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':
    main()      
                                




























