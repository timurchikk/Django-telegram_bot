from django.db import models
from django.db.models.fields import FloatField


class Profile(models.Model):
    user_id = models.CharField(
        verbose_name='User ID',
        max_length=255,
        unique=True
    )
    username = models.CharField(
        verbose_name='Username',
        max_length=255,
        null=True
    )
    balance = models.FloatField(
        verbose_name='Balance',
        default=0
    )
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return str(self.user_id) + ' -> ' + str(self.username)


class Payment(models.Model):
    profile = models.ForeignKey(
        Profile,
        verbose_name='User',
        on_delete=models.PROTECT
    )
    user_id = models.CharField(
        verbose_name='User_ID',
        max_length=255
    )
    number = models.CharField(
        verbose_name='Phone number',
        max_length=50,
        null=True
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма: ',
        null=True
    )
    date = models.DateTimeField(
        verbose_name='Дата вывода'
    )
    status = models.BooleanField(
        verbose_name='Отправлено!',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='Не оплачен',
        default=True
    )

    class Meta:
        verbose_name = 'Заявки для вывода'
        verbose_name_plural = 'Заявки для вывода'

    def __str__ (self):
        return str(self.profile)


class Task(models.Model):
    text = models.TextField(
        verbose_name='Текст задачи'
    )
    url = models.URLField(
        verbose_name='URL задачи'
    )
    create_at = models.DateTimeField(
        verbose_name='Создано',
        auto_now=True
    )
    bon = models.PositiveIntegerField(
        verbose_name='Сумма для выполнения'
    )
    status = models.BooleanField(
        verbose_name='Статус'
    )

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return str(self.id)


class TaskList(models.Model):
    task = models.ForeignKey(
        Task,
        verbose_name='Task',
        on_delete=models.CASCADE,
        unique=True
    )