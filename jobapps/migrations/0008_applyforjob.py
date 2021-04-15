# Generated by Django 3.1.7 on 2021-04-14 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobapps', '0007_auto_20210414_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyForJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(null=True, upload_to='photos/logo/%y/%m/%d')),
                ('resume', models.FileField(blank=True, upload_to='resume/%y/%m/%d')),
                ('cover_letter', models.TextField()),
                ('salary_exceptation', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('job_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobapps.jobpost')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]