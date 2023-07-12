from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
users = [
    {"name": "Sheriff"},
    {"name": "ned"},
    {"name": "Eniola"}
]


def play(request):
    return render(request, 'books/welcome.html', {"Students": list(users)})
