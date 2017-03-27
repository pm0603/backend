from django.conf.urls import url
from member import views


urlpatterns = [
    url(r'^login/$', views.Login.as_view()),
    url(r'^signup/$', views.SignUp.as_view()),

]
