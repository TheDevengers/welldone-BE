# Generated by Django 2.2.5 on 2019-09-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20190912_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(choices=[('PB', 'Published'), ('DR', 'Draft')], default='DR', max_length=2, verbose_name='Article state'),
        ),
    ]