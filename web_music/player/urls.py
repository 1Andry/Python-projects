from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    # path('upload/', model_form_upload, name='model_form_upload'),
    path('', Base.as_view(), name='base'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('upload/', add_song, name='add_song'),
    path('ss/', show_songs, name='show_songs'),
    # path('user_page/', add, name='user_page'),
    # path('user_page/', UserPage.as_view(), name='user_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='player/logout.html'), name='logout'),
    # path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),

]
