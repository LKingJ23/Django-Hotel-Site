# Generated by Django 2.2.2 on 2019-06-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
