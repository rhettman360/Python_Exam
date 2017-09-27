# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..login_app.models import User

# Create your models here.
class Friend(models.Model):
    user = models.ManyToManyField(User, related_name='friends')
