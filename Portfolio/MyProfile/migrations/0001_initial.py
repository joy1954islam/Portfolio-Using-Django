# Generated by Django 3.1.1 on 2020-11-11 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=200, null=True)),
                ('Degree', models.CharField(max_length=200, null=True)),
                ('Major', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('yearDuration', models.CharField(blank=True, max_length=100, null=True)),
                ('result', models.FloatField(null=True)),
                ('StartDate', models.DateField(blank=True, null=True)),
                ('EndDate', models.DateField(blank=True, null=True)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Basic_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pics', models.ImageField(blank=True, null=True, upload_to='')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Phone', models.CharField(max_length=30, null=True)),
                ('Location', models.CharField(max_length=40, null=True)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=30)),
                ('Language', models.ManyToManyField(to='MyProfile.Language')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]