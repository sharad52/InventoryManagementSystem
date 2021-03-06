# Generated by Django 3.0.1 on 2020-02-01 04:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ImageField(null=True, upload_to='media/pics'),
        ),
        migrations.AddField(
            model_name='goods',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
