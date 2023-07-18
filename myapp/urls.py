from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('users/', views.user_list, name='users'),
 
    path('new_user/', views.new_user, name='new_user'),
  

    path('users/<int:user_id>/delete/', views.delete_user, name='delete_user'),
    # path('users/<int:user_id>/update/', views.update_user, name='update_user')
      path('users/<int:user_id>/update/', views.update_user, name='update_user'),
       path('search/', views.search_users, name='search_users') 
]
