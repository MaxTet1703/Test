# Generated by Django 4.2.1 on 2023-06-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Название места'),
        ),
    ]
