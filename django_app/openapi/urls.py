from django.conf.urls import url

from .views import SnippetViewSet
from . import open_api

snippet_list = SnippetViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    url(r'^apitest/area-search/', open_api.Area.as_view()),
    url(r'^apitest/genre-search/', open_api.Genre.as_view()),
    url(r'^apitest/period-search/', open_api.Period.as_view()),
    url(r'^apitest/serializer/', snippet_list),
]
