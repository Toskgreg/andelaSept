# --- accounts.py --
# This file contains code for managing your account
ACCOUNTS=[]

accounts = {}  # dictionary where key is the  password and value is User

# Write a function adds user details to accounts
class Account(object):
    ''' A Accounts class'''

    def __init__(
            self,
            name,
            password):
        ''' Initializes the question object'''
        self.name = name
        self.password = password

    @staticmethod
    def add_account(name, password):
        """
        Adds the key value pair to the accounts dictionary
        """
        accounts['name'] = name
        accounts['password'] = password

        ACCOUNTS.append(accounts)
        return "Your details have been successfully added."


    def login(self,name, password):
        """
        returns true if the password and corresponding name exist in the 
        accounts dicitionary
        """
        if accounts['name'] == name and accounts['password'] == password:
            return True

