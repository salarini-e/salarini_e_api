# Generated by Django 5.1.5 on 2025-01-27 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
