# from django.contrib.auth.base_user import BaseUserManager
#
#
# class CustomUserManager(BaseUserManager):
#
#     def create_user(self, name, email, password=None):
#         if email:
#             email = self.normalize_email(email)
#         else:
#             raise ValueError('Email must be set.')
#         user = self.model(email=email, name=name)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, name, email, password=None):
#         user = self.create_user(name, email, password)
#         user.is_active = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save()
#         return user
