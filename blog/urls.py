from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('login/', views.ulogin, name='login'),
    path('upload/', views.model_form_upload, name='upload'),
    #path('boot', views.boot, name='boot'),
]
