
from api.serializers.books import BookSerializer
from apps.book.models import Book
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class BooksListCreate(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer()
    

class BookUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer()
    lookup_field = 'pk'