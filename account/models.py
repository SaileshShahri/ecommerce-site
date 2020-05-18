import datetime 
import random 
import os 

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
		email=self.normalize_email(email),
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, password):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(
		    email,
		    password=password,
		)
		user.staff = True
		user.save(using=self._db)
		return user


	def create_superuser(self, email, password):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(
		    email,
		    password=password,
		)
		user.staff = True
		user.admin = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	# user data
	name = models.CharField(max_length=300)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=100, null=True)
	phonenumber = models.CharField(max_length=10, validators=[RegexValidator(regex=r'^[0-9]{10}$')])

	# login data
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) 
	admin = models.BooleanField(default=False) 

	# meta data
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return name

	def get_short_name(self):
		return self.email

	@property
	def is_active(self):
		return self.active

	def has_perm(self, perm, obj=None):
		# "Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		# "Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	def has_add_permission(request):
		return True

	@property
	def is_staff(self):
		# "Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		# "Is the user a admin member?"
		return self.admin

