# Generated by Django 4.2.2 on 2023-06-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('post', models.CharField(max_length=200)),
                ('comment', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
