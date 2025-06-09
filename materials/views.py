from django.shortcuts import render, get_object_or_404
from .models import Grade, Topic, Resource

def grade_detail(request, slug):
    grade = get_object_or_404(Grade, slug=slug)
    topics = grade.topics.all().order_by('order')  # Используем related_name="topics"
    return render(request, 'materials/grade_detail.html', {'grade': grade, 'topics': topics})

def topic_detail(request, slug):
    topic = get_object_or_404(Topic.objects.prefetch_related('grades'), slug=slug)
    return render(request, 'materials/topic_detail.html', {'topic': topic})

def textbooks_view(request):
    # Можно добавить фильтрацию ресурсов по типу
    textbooks = Resource.objects.filter(resource_type__in=['TEXT', 'PDF'])
    context = {
        'title': 'Рекомендуемые учебники',
        'textbooks': textbooks,
        'description': 'Подборка лучших учебников для подготовки к олимпиадам'
    }
    return render(request, 'resources/textbooks.html', context)

def video_lessons_view(request):
    videos = Resource.objects.filter(resource_type='VIDEO')
    context = {
        'title': 'Видеоуроки',
        'videos': videos,
        'description': 'Коллекция обучающих видео по олимпиадной физике'
    }
    return render(request, 'resources/video_lessons.html', context)

def olympiad_archive_view(request):
    olympiads = Resource.objects.filter(resource_type='ARCHIVE')
    context = {
        'title': 'Архив олимпиад',
        'olympiads': olympiads,
        'description': 'Задачи прошлых лет с решениями'
    }
    return render(request, 'resources/olympiad_archive.html', context)