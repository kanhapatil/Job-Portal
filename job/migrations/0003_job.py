# Generated by Django 4.1.6 on 2023-05-29 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=500)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=100)),
                ('creationdate', models.DateField()),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.recruiter')),
            ],
        ),
    ]
