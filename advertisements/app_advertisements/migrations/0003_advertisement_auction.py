# Generated by Django 4.2.3 on 2023-08-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0002_advertisement_created_at_advertisement_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отметьте, уместен ли торг', null=True, verbose_name='торг'),
        ),
    ]
