# Generated by Django 5.0.6 on 2024-05-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_link_order_project_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='contact_text',
            field=models.TextField(default='Hello World!'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='language_text',
            field=models.TextField(default=''),
        ),
    ]
