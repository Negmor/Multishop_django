# Generated by Django 4.2.7 on 2024-04-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_alter_discountmodel_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
