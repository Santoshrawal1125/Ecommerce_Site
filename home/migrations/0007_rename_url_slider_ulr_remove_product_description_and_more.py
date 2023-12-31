# Generated by Django 4.2.2 on 2023-07-10 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='url',
            new_name='ulr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rank',
        ),
        migrations.AddField(
            model_name='product',
            name='desription',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='post',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='labels',
            field=models.CharField(blank=True, choices=[('', 'default'), ('new', 'new'), ('sale', 'sale'), ('hot', 'hot')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
