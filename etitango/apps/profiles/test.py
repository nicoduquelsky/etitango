from django.test import TestCase
from .models import Profile, User


#Verify profile creation after User creation
class ProfileCreationAfterUserCreation(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(email='Test@test.com', password='1234') #Dummy user
        
    
    def test_profile_creation_after_user_created(self):
        user_email = 'Test@test.com'
        test_user = User.objects.latest('id') #Last created user. It is the previous dummy user
        test_profile = Profile.objects.filter(email=test_user)
        
        if len(test_profile) == 1:
            if test_profile[0].email == user_email:
                no_profile_flag = False
            else:
                no_profile_flag = True
        else:
            no_profile_flag = True #The profile is missing or is not rigth

        self.assertTrue(no_profile_flag)

#Test User model fields
class UserModelTestData(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Creates data once and it remains as log as the test last. 
        User.objects.create(email='Test@test.com', password='1234')
    
    def test_default_user_model_flag(self): #Test correct user flags
        test_user = User.objects.latest('id')
        
        active_flag = test_user.is_active
        staff_flag = test_user.is_staff
        admin_flag = test_user.is_admin
        superuser_flag = test_user.is_superuser

        #Every flag is false by default. If one is True, there is an error
        self.assertFalse(active_flag or staff_flag or admin_flag or superuser_flag)
    
    #Check correct model label
    def test_email_label(self): 
        test_user = User.objects.latest('id')
        email_label = test_user._meta.get_field('email').verbose_name
        
        self.assertEquals(email_label, 'email')
    
    #Check model field legth
    def test_email_max_length(self):
        test_user = User.objects.latest('id')
        max_length = test_user._meta.get_field('email').max_length
        
        self.assertEquals(max_length, 255)



# class ProfileModelTestData(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         test_user = User.objects.create(email='Test@test.com', password='1234')
#         Profile.objects.create(
#             email = test_user,
#             updated = False,
#             name = 'Test name',
#             last_name = 'LTest last_name',
#             dni_type = 'DNI',
#             dni_number = 325415642,
#             birth_date = 
#         ) 
