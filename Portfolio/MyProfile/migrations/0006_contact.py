# Generated by Django 3.1.1 on 2020-11-11 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyProfile', '0005_auto_20201111_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=17)),
                ('message', models.TextField()),
            ],
        ),
    ]