from django.urls import path
from .import views
from student_management_app import views, HodViews

urlpatterns = [
    path('demo',views.showDemoPage),
    path('',views.showLoginPage),
    path('doLogin',views.doLogin),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),

    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_course/', HodViews.add_course,name="add_course"),
    path('add_course_save', HodViews.add_course_save,name="add_course_save"),

]
