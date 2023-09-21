from django.urls import path
from . import views

urlpatterns = [

    path('', views.my_profile, name='my_profile'),
    path('<int:profile_id>', views.profile_detail, name='profile_detail'),
    path('friends/', views.friends_list, name='friends_list'),
    path('friend/<int:user_id>/', views.send_request_friend, name='send_friend_request'),
    path('accept_friend_request/<int:user_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('rejected_friend_request/<int:user_id>/', views.rejected_friend_request, name='rejected_friend_request'),

]