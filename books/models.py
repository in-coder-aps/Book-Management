from django.db import models


class Book(models.Model):
    bookid = models.IntegerField(unique=True, default=0)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)


class User(models.Model):
    userlist = (('1', 'Admin'), ('2', 'Buyer'), ('3', 'Seller'))
    userid = models.IntegerField(unique=True, default=0)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    usertype = models.CharField(max_length=1, choices=userlist, default='1')


class Order(models.Model):
    orderid = models.IntegerField(unique=True, default=0)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)
