# Generated by Django 2.2.5 on 2019-10-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_merge_20191013_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image_user',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='User Picture'),
        ),
    ]
