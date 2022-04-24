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
    return Credentials.display_credentials()       #returns the credentials list 


def generate_password(self):
    '''
    generate password randomly
    '''
    gen_password=Credentials.generate_password(self)
    return gen_password


def main():                        #this function is responsible for the flow of the application
    print("Hello, welcome to password locker!")
    print('\n')
    print("To login to your account, enter shortcode 'l'; To sign up, enter shortcode 's'; to exit the program enter short code 'e'")

    while True:                     #this is the main loop, it will keep running until the user enters the short code 'e'
        short_code=input().lower()  #The user input is converted to lowercase


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
                print("Wrong username, use shortcode 'na' to create an account")
            elif user_exists !=password:
                print("Invalid password!, use shortcode 'na' to create an account")
                print("*"*60)


        if short_code=="s":        #sign up
            print("-"*60)
            print('To sign up, Enter your account_name')
            account_name=input()
            print('Enter a password')
            account_password=str(input())
            print(f"Account name:{account_name} \n Password:{account_password}")
            print('Write a username, one that you can remember')
            username=input()
            print(f"Hello {username}, logged in! Welcome!")
            print("*"*60)   #prints a line of stars
            save_user(create_user_account(account_password, username))     
            print(f"To create a new account, enter:\n 'na'for a new account,\n  'ex'for an existing account \n")
            short_code = input("").lower().strip()     


        if short_code == "e":      #exit the program
            print("-"*60)
            print("Thank you for using password locker")
            break  


        if short_code=='na':           #create a new user account
            print("Create new account")
            print("Account name:")
            account_name=input()
            print("Username:")
            username=input()
            print("password")
            password=""

            while True:
                print("use shortcode 'Tp' to type your password and 'Gp' to generate a password")
                password_choice = input().lower().strip()
                if password_choice=='tp':
                    password=input("Enter your password \n")
                    break
                
                elif password_choice =='gp':
                    password = input(generate_password(password))
                    print(f"Your password is {password}")
                    break

                else:
                    print("Invalid password")

            save_user(create_user_account(username, password))  
            print("-"*60)
            print(f"Hello {username}, Your {account_name} account  has been created succesfully! Your password is: {password}")
            print("-"*60) 
        
            print("To proceed select shortcodes:\n 'cc' to  Create a new credential \n 'ds' to Display your credentials \n 'fc' to Find a credential \n 'd' to Delete credential \n 'e' to Exit the application \n") 
            short_code = input().lower().strip()
            print("*"*60)

            if short_code=='ex':   #login to an existing account
                print("-"*60)
                print("Welcome to your account!")
                print("-"*60)
                print("To proceed select shortcodes:\n 'cc' to  Create a new credential \n 'ds' to Display your credentials \n 'fc' to Find a credential \n 'd' to Delete credential \n 'e' to Exit the application \n") 
                short_code = input().lower().strip()
                print("*"*60)

            if short_code == "cc":   #creates new credentals
                print("Create new credentials")
                print("-"*80)
                print("Account name:")
                account_name = input().lower()
                print("Your Account username:")
                username = input()
                print(" Use shortcode 'ty' to Type your own pasword if you already have an account:\n Gp - Generate a random Password")
                password_Choice = input().lower().strip()

                if password_Choice=="ty":   #if the user wants to type in their own password
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice=="gp":  #if the user wants to generate a random password
                    password = generate_password(password)
                    break
                else:
                    print("invalid password")
                save_credentials(create_new_credentials(account_name,account_name,account_password))
                print('\n')
                print(f"Account Credential for:Account {account_name} :Username: {username} Password:{password} have been created succesfully")
                print('\n')    

            elif  short_code =="ds":
                print("ACCOUNT DETAILS ARE:")
                print("*-"*40)
                print(' ')

                if display_Credentials(username):
                    print("Here is a list of all your credentials")
                    print(' ')
                    print('\n')
                    for credentials in display_Credentials(username):
                        print(f"Account name: {credentials.account_name} \n Username: {credentials.username} \n Password: {credentials.password}")
                        print(' ')
                        print("To proceed select shortcodes:\n 'cc' to  Create a new credential")
                else:
                    print(' ')
                    print("You don't seem to have any credentials saved yet")
                    print(' ') 

            elif short_code=="fc":
                print("Enter the account name you want to search for")
                search_account = input()
                if find_account(search_account):
                    search_account = find_account(search_account)
                    print(f"{search_account.account_name} {search_account.username} {search_account.password}")
                else:
                    print("Account not found")

            elif short_code=="d":
                print("Enter the account name you want to delete")
                search_account = input()
                if find_account(search_account):
                    search_account = find_account(search_account)
                else:
                    print("Account not found")

                    print(f"Are you sure you want to delete {search_account.account_name}?")
                    print(f"if yes type 'yes' and if no type shortcode 'e' ")

                if type == "y":
                    delete_credentials(search_account)
                    print(f"{search_account.account_name} {search_account.username} {search_account.password}")
                else:
                    print("-"*60)
                    print("Thank you for using password locker")
                    break  
          



if __name__ == '__main__':
    main()