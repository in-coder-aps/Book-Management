from rest_framework import generics, filters,permissions,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from books.serializers import BookSerializer, UserSerializer, OrderSerializer
from .models import Book, User, Order

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BookSearchView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    search_fields = ['title', 'author', 'genre']
    filter_backends = (filters.SearchFilter,)


class UserAPIView(APIView):
    def get(self, request):
        objs = User.objects.all()
        serializer = UserSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'User Added.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})

    def put(self, request):
        value = request.data
        obj = User.objects.get(userid=value['userid'])
        serializer = UserSerializer(obj, data=value)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data, 'message': 'User Details Updated.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})

    def patch(self, request):
        value = request.data
        obj = User.objects.get(userid=value['userid'])
        serializer = UserSerializer(obj, data=value, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data, 'message': 'User Details Updated.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})
    
    def delete(self, request):
        data = request.data
        obj = User.objects.get(userid=data['userid'])
        obj.delete()
        return Response({'status': 200,'message': 'User has been deleted from the Database!'})


class BookAPIView(APIView):
    def get(self, request):
        objs = Book.objects.all()
        serializer = BookSerializer(objs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Book Added.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})

    def put(self, request):
        value = request.data
        obj = Book.objects.get(bookid=value['bookid'])
        serializer = BookSerializer(obj, data=value)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data, 'message': 'Book Details Updated.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})

    def patch(self, request):
        value = request.data
        obj = Book.objects.get(bookid=value['bookid'])
        serializer = BookSerializer(obj, data=value, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 201, 'payload': serializer.data, 'message': 'Book Details Updated.'})
        return Response({'status': 406, 'errors': serializer.errors, 'message': 'Something went wrong!'})
    
    def delete(self, request):
        data = request.data
        obj = Book.objects.get(bookid=data['bookid'])
        obj.delete()
        return Response({'status': 200,'message': 'Book has been deleted from the Database!'})
