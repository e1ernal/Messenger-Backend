from django.db import models


class DirectChat(models.Model):
    first_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Первый участник',
                                   related_name='direct_chats_f')
    second_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Второй участник',
                                    related_name='direct_chats_s')
    hasher_symmetric_key = models.TextField(max_length=255, verbose_name='Зашифрованный симметричный ключ')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    is_private = models.BooleanField(verbose_name='Приватный чат?')

    def __str__(self):
        return f'chat for {self.first_user.username} and {self.second_user.username}'

    class Meta:
        db_table = 'direct_chats'
        app_label = 'models_app'
        verbose_name = 'Direct chat'
        verbose_name_plural = 'Direct chats'
        constraints = [
            models.UniqueConstraint(
                fields=["first_user", "second_user"], name="unique_first_user_second_user"
            ),
        ]
