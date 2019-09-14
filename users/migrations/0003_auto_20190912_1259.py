# Generated by Django 2.2.5 on 2019-09-12 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190910_1913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(null=True, verbose_name='Birth date'),
        ),
        migrations.AlterField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
    ]