from django.db import models


class Message(models.Model):
    author = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, verbose_name='Автор',
                               related_name='messages')
    direct = models.ForeignKey('DirectChat', on_delete=models.CASCADE, verbose_name='Чат',
                               related_name='messages')
    text = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'Message text: {self.text}, time: {self.created_at}'

    class Meta:
        db_table = 'message'
        app_label = 'models_app'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
