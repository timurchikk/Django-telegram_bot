# Generated by Django 3.2.7 on 2021-09-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_alter_profile_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.IntegerField(default=1, verbose_name='Balance'),
            preserve_default=False,
        ),
    ]
