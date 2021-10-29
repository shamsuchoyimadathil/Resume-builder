# Generated by Django 3.2.8 on 2021-10-16 05:08

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('about_you_short', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('skills', models.CharField(max_length=25)),
                ('awards', models.CharField(max_length=250)),
                ('languages', models.CharField(max_length=50)),
                ('interests', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=150)),
                ('school_place', models.CharField(max_length=50)),
                ('degree', models.CharField(max_length=50)),
                ('school_in', models.DateField()),
                ('school_out', models.DateField()),
                ('company_name', models.CharField(max_length=150)),
                ('company_place', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('company_in', models.DateField()),
                ('company_out', models.DateField()),
                ('project_name', models.CharField(max_length=250)),
                ('project_detail', models.TextField()),
            ],
        ),
    ]
