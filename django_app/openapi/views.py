from rest_framework import filters
from rest_framework import viewsets

from .models import Content
from .serializers import ContentSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('seq', 'title', 'start_date', 'end_date', 'place', 'realm_name',
                     'area', 'price', 'content', 'ticket_url', 'phone', 'thumbnail',
                     'place_url', 'place_addr')

    def list(self, request, *args, **kwargs):
        print(request.data)
        print(request.GET)
        return super().list(request, *args, **kwargs)
