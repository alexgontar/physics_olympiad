# Generated by Django 5.2.1 on 2025-05-30 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0002_remove_resource_topic_resource_topics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='grade',
        ),
        migrations.AddField(
            model_name='topic',
            name='grades',
            field=models.ManyToManyField(related_name='topics', to='materials.grade'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
