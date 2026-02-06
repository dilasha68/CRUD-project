from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/read/<int:id>/', views.read_one, name='read_one'),
    path('blog/update/<int:id>/', views.update_one, name='update_one'),
    path('blog/delete/<int:id>/', views.delete_one, name='delete_one'),
]
