from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lessons/', views.LessonListView.as_view(), name='lessons'),
    path('lesson/<int:pk>', views.LessonDetailView.as_view(), name='lesson-detail'),
]