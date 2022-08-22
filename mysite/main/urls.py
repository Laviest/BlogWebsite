from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path('create_blog/', views.create_blog, name='create_blog'),
    path('update_blog/<int:id>', views.update_blog, name='update_blog'),
    path('my_profile/', views.my_profile, name="my_profile"),
    path('other_profile/<int:id>', views.view_other_profile, name="other_profile"),
    path("edit/<int:id>", views.edit_blog, name="edit_blog")
]