# Generated by Django 3.2.7 on 2021-09-30 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_auto_20210930_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='is_active'),
            preserve_default=False,
        ),
    ]