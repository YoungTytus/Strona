# Generated by Django 4.1.7 on 2023-03-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_snippet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.TextField(max_length=200),
        ),
    ]
