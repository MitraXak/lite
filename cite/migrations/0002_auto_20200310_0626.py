# Generated by Django 2.2.11 on 2020-03-10 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='nametheme',
        ),
        migrations.AddField(
            model_name='theme',
            name='nametheme',
            field=models.ManyToManyField(to='cite.Kurs'),
        ),
    ]
