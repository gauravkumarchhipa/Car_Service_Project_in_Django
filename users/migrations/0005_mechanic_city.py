# Generated by Django 4.0.3 on 2022-06-25 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_mechanic_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
    ]