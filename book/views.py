from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome(requests):
    return render(requests, 'books/welcome.html', {"name": "Asa"})


def hello(request):
    return HttpResponse("Hello from book app")

def get_books(request):
    return HttpResponse("List of all books")
