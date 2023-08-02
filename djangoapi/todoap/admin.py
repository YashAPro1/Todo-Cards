from django.contrib import admin
from .models import Todomodel, User
# Register your models here.

admin.site.register(Todomodel)
admin.site.register(User)