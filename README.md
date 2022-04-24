# PASSWORD-LOCKER

## Built By [Gladys Wambura](https://github.com/gladyswambura/)

## Description
Password Locker is a terminal-run-python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

A user can:
* Create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Welcome, choose an option: c-Create Account, l-Log In, e-Exit |
| Display prompt for creating an account | **Enter: c** | Enter your Account_name, Account_password and Account_username |
| Display prompt for login in | **Enter: l** | Enter your user_name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the Account_name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Exit application | **Enter: e** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.8
* pip
* pyperclip
* xclip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/gladyswambura/Password-Locker/
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.8 test_credentials.py
        $ python3.8 test_user.py
        
## Technologies Used
* Python3.8

## Further help
https://www.linkedin.com/in/gladys-wahito-wambura/

## MIT License
Copyright (c) [2022] [Gladys Wambura]. All Rights Reserved.
<a href="./LICENSE"> LICENSE</a>

## Authors Info

Slack Profile - [Gladys Wambura](https://stackoverflow.com/users/18241026/gladys-wahito?tab=profile)

Linked - [Gladys Wambura](https://www.linkedin.com/in/gladys-wahito-3480a01ab/)
