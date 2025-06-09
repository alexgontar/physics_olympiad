from django.db import models
from django.utils.text import slugify


class Grade(models.Model):
    number = models.IntegerField(unique=True)  # 7, 8, 9, 10, 11
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)  # Для ЧПУ-URL (например, "grade-9")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"grade-{self.number}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number} класс"


class Topic(models.Model):
    grades = models.ManyToManyField(Grade, related_name="topics")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def resource_count(self):
        return self.resources.count()

    def __str__(self):
        return self.title


class Resource(models.Model):
    RESOURCE_TYPES = [
        ('PDF', 'PDF-файл'),
        ('VIDEO', 'Видео'),
        ('LINK', 'Ссылка'),
        ('TEXT', 'Текстовая статья'),
        ('ARCHIVE', 'Архивы олимпиад')
    ]

    topics = models.ManyToManyField('Topic', related_name="resources")
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=7, choices=RESOURCE_TYPES)
    file = models.FileField(upload_to="resources/", blank=True, null=True)  # Для PDF
    url = models.URLField(blank=True)  # Для видео или ссылок
    content = models.TextField(blank=True)  # Для статей
    created_at = models.DateTimeField(auto_now_add=True)

    def has_both(self):
        """Проверяет, есть ли у ресурса и файл, и ссылка"""
        return self.file and self.url

    def __str__(self):
        return self.title
