# Generated by Django 2.2.5 on 2019-09-23 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_merge_20190923_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='DR', max_length=2, verbose_name='Article state'),
        ),
    ]
