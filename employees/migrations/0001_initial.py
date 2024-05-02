# Generated by Django 4.0.8 on 2024-04-27 10:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=255)),
                ('is_married', models.BooleanField(default=False)),
                ('salary', models.FloatField(default=0.0)),
                ('contract_exp', models.DateTimeField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
            ],
        ),
    ]
