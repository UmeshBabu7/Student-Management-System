from django.urls import path
from .import views

urlpatterns = [
    path('demo',views.showDemoPage),
    path('',views.showLoginPage),
    path('doLogin',views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
]
