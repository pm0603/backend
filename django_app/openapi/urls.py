from django.conf.urls import url

from . import open_api
from .views import SnippetViewSet, DetailViewSet, AreaViewSet, GenreViewSet

snippet_list = SnippetViewSet.as_view({
    'get': 'list'
})
snippet_detail = DetailViewSet.as_view({
    'get': 'list'
})
snippet_area = AreaViewSet.as_view({
    'get': 'list'
})
snippet_genre = GenreViewSet.as_view({
    'get': 'list'
})
urlpatterns = [
    # 지역별 검색 DB 추가
    url(r'^apitest/area-search/', open_api.Area.as_view()),
    # 분야별 검색 DB 추가
    url(r'^apitest/genre-search/', open_api.Genre.as_view()),
    # 기간별 검색 DB 추가
    url(r'^apitest/period-search/', open_api.Period.as_view()),
    # DB에서 원하는 키워드로 검색
    url(r'^apitest/serializer/', snippet_list),
    # Detail 검색 (search= seq, title)
    url(r'^apitest/detail', snippet_detail),
    # 지역별 검색 (search= area)
    url(r'^apitest/area', snippet_area),
    # 분야별 검색 (search= genre)
    url(r'^apitest/genre', snippet_genre),
]
