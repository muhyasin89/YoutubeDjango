

from api.serializers.author import AuthorSerializer
from apps.author.models import Author
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class AuthorsListCreate(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer = AuthorSerializer()
    

class AuthorUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer = AuthorSerializer()
    lookup_field = 'pk'