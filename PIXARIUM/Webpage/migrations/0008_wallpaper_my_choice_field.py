# Generated by Django 4.1.4 on 2023-03-19 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0007_alter_wallpaper_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallpaper',
            name='my_choice_field',
            field=models.CharField(choices=[('AN', 'Anime'), ('GM', 'Games'), ('MV', 'Movies')], default='AN', max_length=2),
        ),
    ]