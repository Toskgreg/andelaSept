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
    def validate_email(email):
        email_regex = re.compile(r"^[A-Za-z0-9_-]+@[A-Za-z0-9_-]+\.[a-zA-Z]*$")
        if not email_regex.match(email):
            print('invalid email')
            raise ValueError("Wrong email format")
        else:
            print('valid email')
            print(email)
            return email

    @staticmethod
    def validate_age(age):
        r = re.compile(r"^[1-9]{1,3}$")
        if not r.search(age):
            raise ValueError("Wrong age")
        else:
            print('valid age')
            print(age)
            return age

    @staticmethod
    def validate_password(password):

        rule = re.compile(r"^[A-Za-z0-9@!#]{4,}$")
        if not rule.search(password):
            print("Invalid Password.")
            raise ValueError("Wrong password")
        else:
            return password

    @staticmethod
    def validate_username(username):
        if not re.match("^[a-zA-Z0-9_]*$",username):
            print('invalid username')
            raise ValueError("Wrong username format")
        else:
            print('valid username')
            print(username)
            return username

    @staticmethod
    def create_user(username ,first_name, last_name, age, email,password):
        """
        Adds the user (string value) to user_list
        """ 
        user['Id'] = uuid.uuid1()
        user['username'] = SignUp.validate_username(username)
        user['first_name'] =first_name
        user['last_name'] = last_name
        user['age'] = SignUp.validate_age(age)
        user['email'] = SignUp.validate_email(email)
        user['password'] = SignUp.validate_password(password)
        Users.append(user)
        return 'You are registered'

    @staticmethod
    def login(username ,password):
        for x in Users:
            if x['username'] == user['username'] and x['password'] == user['password']:
                return "Your successfully logged in. "

    @classmethod
    def update(cls,username ,first_name, last_name, age, email,password):
        for x in Users:
            if x['username'] == user['username'] and x['password'] == user['password']:
                cls.user1={}
                cls.user1['username'] = username
                cls.user1['first_name'] =first_name
                cls.user1['last_name'] = last_name
                cls.user1['age'] = age
                cls.user1['email'] = email
                cls.user1['password'] = password
                Users.append(user.update(cls.user1))
                return "Your successfully updated. "
                
