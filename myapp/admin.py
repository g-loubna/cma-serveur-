from django.contrib import admin
from myapp.models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


admin.site.register(NewUser)
admin.site.register(CreateSuggestioncomplaints)
