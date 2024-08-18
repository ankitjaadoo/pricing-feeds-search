from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_csv, name='upload_csv'),
    path('search/', views.search_records, name='search_records'),
    path('edit/<int:pk>/', views.edit_record, name='edit_record'),
]