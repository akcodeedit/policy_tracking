from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('admin/', views.admin_login, name='admin_login'),
    path('change_password/', views.change_password, name='change_password'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('add_policy/', views.add_policy, name='add_policy'),
    path('delete_policy/<id>', views.delete_policy, name='delete_policy'),
    path('view_policy/<id>', views.view_policy, name='view_policy'),
    path("edit_policy/<id>", views.edit_policy, name='edit_policy'),
    path('all_policy/', views.all_policy, name='all_policy'),
    path('search_policy/', views.search_policy, name='search_policy'),
]