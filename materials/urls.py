from django.urls import path
from .views import grade_detail, topic_detail, textbooks_view, video_lessons_view, olympiad_archive_view

urlpatterns = [
    path('grade/<slug:slug>/', grade_detail, name='grade_detail'),
    path('topic/<slug:slug>/', topic_detail, name='topic_detail'),
    path('textbooks/', textbooks_view, name='textbooks'),
    path('video_lessons/', video_lessons_view, name='video_lessons'),
    path('olympiad_archive/', olympiad_archive_view, name='olympiad_archive'),
]