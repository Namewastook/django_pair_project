from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.home, name="Home"),
    path('signup/', views.SignUp.as_view(), name='SignUp'),
    path('Profile/', views.profile_create, name='ProfileCreate'),
    path("add/", views.add_profile, name="Add"),
    path("update/<int:id>", views.update_profile, name="update")
]
