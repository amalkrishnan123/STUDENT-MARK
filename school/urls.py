from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin-dashboard/',views.admin_dashboard,name='admin_dash'),
    path('create-student/',views.create_student,name='create_student'),
    path('edit-student/<int:id>/',views.edit_student,name='edit'),
    path('delete-student/<int:id>/',views.delete_student,name='delete'),
    path('admin-logout/',views.admin_logout,name='admin_logout'),


]
