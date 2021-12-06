from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    link = models.ForeignKey('Link', on_delete=models.PROTECT, verbose_name='Ссылка')
    queue = models.PositiveIntegerField(unique=False, blank=True, verbose_name='Очередь показа')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    image = models.ImageField(blank= False, verbose_name='Изображение')
    image_mobile = models.ImageField(blank=False, verbose_name='Мобильное изображение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Завершить показ')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('time_create',)
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"


class Link(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ссылка')
    path = models.CharField(max_length= 100, verbose_name='Путь')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image = models.ImageField(blank= False, verbose_name='Изображение')
    text = models.TextField(blank=True, verbose_name='Текст')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    end_date = models.DateField(default=None, null=True, blank=True, verbose_name='Завершить показ')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('time_create',)
        verbose_name = "Контент"
        verbose_name_plural = "Контент"


class Appointment(models.Model):
    service = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Услуга')
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT, verbose_name='Клиент')
    master = models.ForeignKey('Master', on_delete=models.PROTECT, verbose_name='Мастер')
    datetime = models.DateTimeField(verbose_name='Дата и время')
    # durations_service_time = models.ForeignKey('Service', on_delete=models.PROTECT, verbose_name='Длительность')

    # def __str__(self):
    #     return self.service

    class Meta:
        ordering = ('datetime',)
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT, verbose_name='Пол')
    phone_number = models.CharField(max_length=12, verbose_name="Номер телефона")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Gender(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пол')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    durations_service_time = models.PositiveIntegerField(verbose_name='Длительность [мин]')
    price = models.DecimalField(max_digits=9, decimal_places=0, verbose_name='Стоимость [₽]')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Master(models.Model):
    name = models.CharField(max_length=255, verbose_name="Мастер")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"

