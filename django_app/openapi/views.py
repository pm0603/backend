from rest_framework import filters
from rest_framework import viewsets

from .models.content import Content
from .serializers import ContentSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                     'area', 'price', 'phone')
