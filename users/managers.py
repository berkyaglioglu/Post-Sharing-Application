from django.contrib.auth.models import BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password):
        user = self.model(email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email=email, first_name=first_name, last_name=last_name, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

