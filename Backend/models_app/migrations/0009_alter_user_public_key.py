# Generated by Django 4.0 on 2024-05-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0008_rename_encrypted_key_directchat_hasher_symmetric_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='public_key',
            field=models.TextField(max_length=255, verbose_name='Публичный ключ'),
        ),
    ]
