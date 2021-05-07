# Generated by Django 3.2 on 2021-05-06 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_title', models.CharField(max_length=200)),
                ('movie', models.CharField(max_length=100, null=True)),
                ('nickname', models.CharField(max_length=100)),
                ('upload_date', models.DateTimeField()),
                ('review_body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/')),
            ],
        ),
    ]
