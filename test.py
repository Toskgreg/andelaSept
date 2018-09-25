import unittest
from auth import SignUp,user,Users


class TestApp(unittest.TestCase):
    


    def test_validate_email_value_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_email('greg@gmail.com-=')

    def test_validate_email_returns_email(self):
        signup = SignUp.validate_email('greg@gmail.com')
        self.assertEqual(signup, 'greg@gmail.com')

    def test_validate_password_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_password('olo')

    def test_validate_password_returns_paasword(self):
        signup = SignUp.validate_password('A@aolo')
        self.assertEqual(signup, 'A@aolo')
    
    def test_validate_username_value_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_username('t greg')

    def test_validate_username_returns_username(self):
        signup = SignUp.validate_username('tgreg')
        self.assertEqual(signup, 'tgreg')

    def test_validate_age_value_error(self):
        with self.assertRaises(ValueError):
            SignUp.validate_age('t')

    def test_validate_age_returns_age(self):
        signup = SignUp.validate_age('1')
        self.assertEqual(signup, '1')

    def test_validate_register(self):

        signup=SignUp.create_user(password='yolo',age='7',email='A@a.com',username='q',first_name='q',last_name='vv')
        
        self.assertEqual('You are registered',
            str(signup))
    
    def test_validate_login(self):
        SignUp.create_user(password='yolo',age='7',email='A@a.com',username='q',first_name='q',last_name='vv')

        login=SignUp.login(password='yolo',username='q')
        
        self.assertEqual('Your successfully logged in. ',
            str(login))
        
    def test_validate_update(self):
        SignUp.create_user(password='yolo',age='7',email='A@a.com',username='q',first_name='q',last_name='vv')
        SignUp.login(password='yolo',username='q')
        update=SignUp.update(password='yoloy',age='8',email='g@a.com',username='w',first_name='x',last_name='v') 
        self.assertEqual("Your successfully updated. ",
            str(update))
    
   
            


if __name__ == '__main__':
    unittest.main()