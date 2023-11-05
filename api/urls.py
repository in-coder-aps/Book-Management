from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookSearchView, UserAPIView,BookAPIView
from books.views import OrderViewSet, BookViewSet

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'order', OrderViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('search/', BookSearchView.as_view(), name='book-search'),
    path('user/', UserAPIView.as_view(), name='user-api'),
    path('book/', BookAPIView.as_view(), name='book-api'),
]
