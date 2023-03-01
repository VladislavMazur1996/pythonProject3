# Generated by Django 4.1.6 on 2023-03-01 05:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_category_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='subscriber',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]