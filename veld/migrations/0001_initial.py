# Generated by Django 3.2.7 on 2021-12-21 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('path', models.CharField(max_length=100, verbose_name='Путь')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('text', models.TextField(blank=True, verbose_name='Текст')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Завершить показ')),
            ],
            options={
                'verbose_name': 'Контент',
                'verbose_name_plural': 'Контент',
                'ordering': ('time_create',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('durations_service_time', models.PositiveIntegerField(verbose_name='Длительность [мин]')),
                ('price', models.DecimalField(decimal_places=0, max_digits=9, verbose_name='Стоимость [₽]')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, verbose_name='Номер телефона')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('queue', models.PositiveIntegerField(blank=True, verbose_name='Очередь показа')),
                ('is_published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('image_mobile', models.ImageField(upload_to='', verbose_name='Мобильное изображение')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('end_date', models.DateField(blank=True, default=None, null=True, verbose_name='Завершить показ')),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='veld.link', verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Баннер',
                'verbose_name_plural': 'Баннеры',
                'ordering': ('time_create',),
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(verbose_name='Дата и время')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='veld.customer', verbose_name='Клиент')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='veld.master', verbose_name='Мастер')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='veld.service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ('datetime',),
            },
        ),
    ]
