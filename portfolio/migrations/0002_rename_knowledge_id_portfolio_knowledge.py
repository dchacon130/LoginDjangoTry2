# Generated by Django 3.2.12 on 2022-04-08 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portfolio',
            old_name='knowledge_id',
            new_name='knowledge',
        ),
    ]