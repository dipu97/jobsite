# Generated by Django 3.1.7 on 2021-04-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0009_auto_20210414_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyforjob',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
