# Generated by Django 4.1.7 on 2023-03-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_category_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='coding', max_length=200),
        ),
    ]