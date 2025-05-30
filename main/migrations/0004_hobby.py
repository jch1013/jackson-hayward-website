# Generated by Django 5.2 on 2025-05-15 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='hobby_images/')),
            ],
        ),
    ]
