# Generated by Django 4.0.5 on 2022-06-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
