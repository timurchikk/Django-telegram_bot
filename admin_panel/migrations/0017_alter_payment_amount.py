# Generated by Django 3.2.7 on 2021-10-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0016_auto_20211001_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.PositiveIntegerField(null=True, verbose_name='Сумма: '),
        ),
    ]
