from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.

# 아이디 = get_user_model()

class 아이디(AbstractUser):
	pass
	# nickname = models.CharField(max_length=15)

class Sale(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	age = models.IntegerField(default=0)
	person = models.ForeignKey("Person", on_delete=models.CASCADE)
	# person = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True)
	# person = models.ForeignKey("Person", on_delete=models.SET_DEFAULT, null=True, default=...)
	def __str__(self):
		return f"이름 : {self.last_name}{self.first_name}"

class Person(models.Model):
	회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)
	# first_name = models.CharField(max_length=30)
	# last_name = models.CharField(max_length=30)
	def __str__(self):
		# return self.회원.email
		return self.회원.username

#----------------------------------------------------------

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class 아이디(AbstractUser):
# 	pass

# class Sale(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	age = models.IntegerField(default=0)
# 	person = models.ForeignKey(아이디, on_delete=models.CASCADE)