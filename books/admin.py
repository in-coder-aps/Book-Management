from django.contrib import admin
from books.models import Book, User, Order
# Register your models here.

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Order)
