# Generated by Django 3.1.3 on 2021-01-14 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='specialization',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
