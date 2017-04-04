import django_filters
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

class DetailViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('seq', 'title')

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('area', 'area')

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('realm_name', 'realm_name')

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('realm_name', 'realm_name')

class PeriodFilter(django_filters.rest_framework.FilterSet):
    start_date = django_filters.NumberFilter(name="price", lookup_expr='gte')
    end_date = django_filters.NumberFilter(name="price", lookup_expr='lte')

    class Meta:
        model = Content
        fields = ['start_date', 'end_date']

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('start_date', 'end_date')
    filter_class = PeriodFilter

