# Generated by Django 4.0.8 on 2024-06-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0013_home_alter_og_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sub_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Home',
        ),
    ]
