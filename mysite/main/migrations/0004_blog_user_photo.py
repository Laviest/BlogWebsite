# Generated by Django 4.1 on 2022-08-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_blog_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='user_photo'),
        ),
    ]