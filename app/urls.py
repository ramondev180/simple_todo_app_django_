from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create-task/', views.create_task, name="create_task"),  
    path('edit-task/<int:pk>', views.edit_task, name="edit_task"),
    path('delete-task/<int:pk>', views.delete_task, name="delete_task"),
]