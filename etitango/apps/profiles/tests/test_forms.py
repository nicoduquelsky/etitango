from datetime import datetime

from django.test import SimpleTestCase, TestCase
from django.utils import timezone

from apps.profiles.forms import UserForm, ProfileForm, RegisterForm

profile_form_data = {'name':'Test Name', 'last_name':'Last Last', 'dni_type':'DNI',
                    'dni_number':'33655465','birth_date':datetime(1980, 12, 31),
                    'gender':'M', 'country':1, 'province':1, 'province':1}

# class UserAdminFormTest(SimpleTestCase):
#     def setUpClass(self):
#         self.user_form = RegisterForm(data={'email':'test@user.com', 
#                                     'password1':'1234', 
#                                     'password2':'1234'})
    
#     def test_user_form_password_label(self):
#         label_pass1 = self.user_form.fields['password1'].label == 'Contraseña'
#         label_pass2 = self.user_form.fields['password2'].label == 'Confirmar Contraseña'
        
#         self.asserTrue(label_pass1 and label_pass2)

# class UserAdminFormTest(SimpleTestCase):
#     @classmethod
#     def setUpClass(self):
#         self.user_form = RegisterForm(data={'email':'test@user.com', 
#                                     'password1':'1234', 
#                                     'password2':'1234'})
    
#     def test_user_form_password_label(self):
#         label_pass1 = self.user_form.fields['password1'].label == 'Contraseña'
#         label_pass2 = self.user_form.fields['password2'].label == 'Confirmar Contraseña'
        
#         self.asserTrue(label_pass1 and label_pass2)

class UserProfileFormTest(TestCase):
    def test_user_form_email_label(self):
        user_form = UserForm()
        label_email = user_form.fields['email'].label == 'Email'

        self.assertTrue(label_email)

    # def test_proper_profile_form(self):
    #     self.databases = '__all__'
    #     profile_form = ProfileForm(data=profile_form_data)
    #     self.assertTrue(profile_form.is_valid())
    
    # def test_actual_date_of_birth(self):
    #     actual_date = datetime.now()
    #     profile_form_data['birth_date'] = actual_date
    #     profile_form = ProfileForm(data=profile_form_data)
                
    #     self.assertFalse(profile_form.is_valid())

