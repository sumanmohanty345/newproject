# Generated by Django 2.2.3 on 2020-02-03 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='Namaste.jpg', upload_to='profile/'),
        ),
    ]
