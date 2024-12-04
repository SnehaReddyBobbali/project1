from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.student_create, name='student_create'),
    path('', views.student_list, name='student_list'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
]
