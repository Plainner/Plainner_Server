from django.shortcuts import render, redirect
from django.db import connection
import datetime
import os
from django.conf import settings
from myApp.models import User, Todo

def mainPage(request):
    data = User.objects.all()
    print(data)