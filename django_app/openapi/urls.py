from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^apitest/area-search/', views.Area.as_view()),
    url(r'^apitest/genre-search/', views.Genre.as_view()),
    url(r'^apitest/period-search/', views.Period.as_view()),
    url(r'^apitest/detail/', views.Detail.as_view()),
]
