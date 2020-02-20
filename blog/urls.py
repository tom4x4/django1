from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('accounts/login/', views.ulogin, name='login'),
    #path('boot', views.boot, name='boot'),
]
