# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def creator(self, postData):
        user = self.create(first_name = postData['name'], alias = postData['alias'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()), birthday = postData['birthday'])
        return user

    def steveCreator(self, postData):
        user = self.create(first_name = 'Steve', alias = postData['alias'], email = postData['email'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()), birthday = postData['birthday'])
        return user

    def validate(self, postData):
        results = {'status': True, 'errors': [], 'isRay': False}
        if len(postData['name']) < 3:
            results['errors'].append('Your first name is too short')
            results['status'] = False
        if postData['name'] == 'Ray' or postData['name'] == 'ray':
            results['isRay'] = True
        if len(postData['alias']) < 3:
            results['errors'].append('Your alias is too short')
            results['status'] = False
        if not re.match(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b', postData['email']):
            results['errors'].append('Your email is not valid')
            results['status'] = False
        if postData['password'] != postData['password_c']:
            results['errors'].append("Your passwords don't match")
            results['status'] = False
        if len(postData['password']) < 8:
            results['errors'].append("Your password is too short")
            results['status'] = False
        if len(self.filter(email = postData['email'])) > 0:
            results['errors'].append("User already exists")
            results['status'] = False
        if len(postData['birthday']) < 8:
            results['errors'].append('Invalid birthday')
            results['status'] = False

        return results

    def loginVal(self, postData):
        results = {'status': True, 'errors': []}
        users = self.filter(email = postData['email'])
        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['password'].encode(),users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False
        return results

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    alias = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
    birthday = models.CharField(max_length = 15)
    objects = UserManager()
