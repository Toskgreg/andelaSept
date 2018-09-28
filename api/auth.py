from flask import jsonify, request
import json
import re
import uuid

Users=[]
user={}


class SignUp(object):
    
    def __init__(self,Id,username ,first_name, last_name, age, email,password):
        self.Id=Id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age =age
        self.password = password
        self.email = email


    @staticmethod
    def create_user():
        """
        Adds the user (string value) to user_list
        """ 
        x=request.get_json()
        username = x.get('username')
        first_name = x.get('firstname')
        last_name=x.get('lastname')
        age = x.get('age')
        email = x.get('email')
        password=x.get('password')
        Id=uuid.uuid1()
        user = SignUp(Id,username ,first_name, last_name, age, email,password)
        Users.append(user)
        return 'You are registered'

    @staticmethod
    def login():
        x=request.get_json()
        username = x.get('username')
        password=x.get('password')
        for x in Users:
            if x['username'] == user['username'] and x['password'] == user['password']:
                return "Your successfully logged in. "
    @staticmethod
    def logOut():
        for x in Users:
            if x['username'] == user['username'] and x['password'] == user['password']:
                break

    @staticmethod
    def delete_account(Id):
        """
        Removes the specified account from Users
        """
        if Id == Id:
            Users.pop()