from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from ninja import ModelSchema


# Create your views here.

def home(request):
    return HttpResponse('SIREG')

def about(request):
    return HttpResponse('<h1>Welcome to About Page</h1>')

# Create your views here.

    