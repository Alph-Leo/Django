from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

# class User(models.Model):
# first_name = models.CharField(max_length=200)
# last_name = models.CharField(max_length=200)
# email = models.EmailField(unique=True)
# phone_number = models.CharField(max_length=11)
# password = models.CharField(max_length=20)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)


class Book(models.Model):
    GENRE_CHOICES = [
        ('FICTION', 'Fiction'),
        ('FINANCE', 'Finance'),
        ('POLITICS', 'Politics'),
        ('ROMANCE', 'Romance')
    ]
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=8, choices=GENRE_CHOICES, default="Finance")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
