# Generated by Django 3.2.7 on 2021-10-01 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0014_alter_profile_balance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name='User_ID')),
                ('number', models.CharField(max_length=50, verbose_name='Phone number')),
                ('amount', models.PositiveIntegerField(verbose_name='Выведено: ')),
                ('date', models.DateTimeField(verbose_name='Дата вывода')),
                ('status', models.BooleanField(verbose_name='Отправлено!')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_panel.profile', verbose_name='User')),
            ],
            options={
                'verbose_name': 'История платежей',
                'verbose_name_plural': 'Истории платежей',
            },
        ),
        migrations.DeleteModel(
            name='PaymantHistory',
        ),
    ]
