# Generated by Django 4.1.4 on 2023-03-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0010_wallpaper_combined_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='Sauce',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
