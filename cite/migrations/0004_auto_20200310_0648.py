# Generated by Django 2.2.11 on 2020-03-10 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cite', '0003_auto_20200310_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='nametheme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cite.Kurs'),
        ),
    ]
