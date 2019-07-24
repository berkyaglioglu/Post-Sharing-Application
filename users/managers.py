from django.contrib.auth.models import BaseUserManager


class Manager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, gender):
        user = self.model(email=email, first_name=first_name, last_name=last_name, gender=gender)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password, gender):
        user = self.model(email=email, first_name=first_name, last_name=last_name, is_superuser=True, is_staff=True, gender=gender)
        user.set_password(password)
        user.save()
        return user

