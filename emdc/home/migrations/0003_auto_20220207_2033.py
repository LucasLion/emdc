# Generated by Django 3.2.12 on 2022-02-07 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20220207_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='video/%y')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadVideo',
        ),
    ]
