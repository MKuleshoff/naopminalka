# Generated by Django 3.0.2 on 2020-01-23 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('napominalka', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
        ),
    ]
