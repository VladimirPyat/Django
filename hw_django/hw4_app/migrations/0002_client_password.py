# Generated by Django 5.0.4 on 2024-04-14 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw4_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
    ]