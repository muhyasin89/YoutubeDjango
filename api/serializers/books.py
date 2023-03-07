from apps.author.models import Author
from apps.book.models import Book
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class BookSerializer(ModelSerializer):
    def to_internal_value(self, data):
        self.fields['author'] = PrimaryKeyRelatedField(
            queryset  = Author.objects.all()
        )

        return super(BookSerializer, self).to_internal_value(data)

    def to_representation(self, instance):
        data = super(BookSerializer, self).to_representation(instance)
        data['display_author'] = instance.author if instance else None

        return data

    class Meta:
        model = Book