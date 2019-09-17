# Generated by Django 2.2.5 on 2019-09-15 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20190912_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publication_date',
            field=models.DateTimeField(null=True, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='state',
            field=models.CharField(choices=[('DR', 'Draft'), ('PB', 'Published')], default='DR', max_length=2, verbose_name='Article state'),
        ),
    ]