from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Добро пожаловать на мой сайт!</h1>')

def data(request):
    return HttpResponse('''
            <h1>Поток данных</h1>
            <img src="/static/images/1.jpg" alt="Data Image" width="300">
        ''')

def test(request):
    return HttpResponse('''
            <h1>Мастерская тестирования</h1>
            <img src="/static/images/2.jpg" alt="Test Image" width="300">
        ''')
