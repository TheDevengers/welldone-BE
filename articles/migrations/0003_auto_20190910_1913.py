# Generated by Django 2.2.5 on 2019-09-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20190907_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='DR', max_length=2, verbose_name='Article state'),
        ),
    ]
