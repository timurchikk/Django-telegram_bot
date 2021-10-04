# Generated by Django 3.2.7 on 2021-10-01 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0015_auto_20211001_1124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Заявки для вывода', 'verbose_name_plural': 'Заявки для вывода'},
        ),
        migrations.AddField(
            model_name='payment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Не оплачен'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Отправлено!'),
        ),
    ]
