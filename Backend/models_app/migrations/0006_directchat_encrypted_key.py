# Generated by Django 4.0 on 2024-03-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='directchat',
            name='encrypted_key',
            field=models.CharField(default=1, max_length=255, verbose_name='Зашифрованный симметричный ключ'),
            preserve_default=False,
        ),
    ]