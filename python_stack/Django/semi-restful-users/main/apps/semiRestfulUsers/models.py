from __future__ import unicode_literals

from django.db import models
import re

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class userManager(models.Manager):
    def user_validator(self, postData):
        errors ={
            
        }
        if len(postData['first_name'])< 3:
            errors['first_name'] = "First name should be more than 3 characters"
            print "I found a validation error"
        if len(postData['last_name'])< 3:
            errors['Last Name'] = "Llast name should be more than 3 characters"
            print "I found a validation error"
        if not NAME_REGEX.match(postData['first_name']):
            errors['First name Format'] = "First name can only have characters"
            print "I found a validation error"
        if not NAME_REGEX.match(postData['last_name']):
            errors["Last Name Format"] = "Last name can only have characters"
            print "I found a validation error"
        if not EMAIL_REGEX.match(postData['email']):
            errors['Email Format'] = "Email is not in proper format"
            print "I found a validation error"
        
        return errors
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, default="Beuler")
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()