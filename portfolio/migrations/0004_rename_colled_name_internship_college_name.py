# Generated by Django 4.2.3 on 2023-07-31 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_internship'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internship',
            old_name='colled_name',
            new_name='college_name',
        ),
    ]