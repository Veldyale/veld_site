# Generated by Django 3.2.7 on 2021-11-30 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veld', '0003_auto_20211123_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('end_date', models.DateTimeField(verbose_name='Дата завершения включительно')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ('time_create',),
            },
        ),
    ]
