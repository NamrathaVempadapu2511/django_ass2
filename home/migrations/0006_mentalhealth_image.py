# Generated by Django 5.0.6 on 2024-07-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_home_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentalhealth',
            name='image',
            field=models.ImageField(default='', upload_to='Mentalhealth/images'),
        ),
    ]
