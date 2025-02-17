from django.urls import path
from .import views

urlpatterns = [
    path('demo',views.showDemoPage),
    path('',views.showLoginPage),
    path('doLogin',views.doLogin)
]
