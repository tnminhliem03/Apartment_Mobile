# Generated by Django 5.0.4 on 2024-05-21 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0003_resident_birthday_resident_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='resident',
        ),
    ]