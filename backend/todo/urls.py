from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.DetailTodo.as_view(), name='detail_todo'),
    path('', views.ListTodo.as_view(), name='list_todo'),
]