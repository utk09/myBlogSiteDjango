from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^details/(?P<id>\d+)/$', views.details, name = 'details')
    #path('<int:id>/', views.details, name = "details")
]
