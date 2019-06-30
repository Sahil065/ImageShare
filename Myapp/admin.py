# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Myapp.models import UserModel,PostModel
# Register your models here.
admin.site.register(UserModel)
admin.site.register(PostModel)