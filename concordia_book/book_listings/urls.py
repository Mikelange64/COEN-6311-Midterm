from django.urls import path
from . import views

urlpatterns = [
    path('textbooks/<str:course_code>/', views.textbook_list, name='textbook_list'),
]