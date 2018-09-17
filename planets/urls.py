from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from planets import views

urlpatterns = [
    url(r'^planets', views.PlanetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
