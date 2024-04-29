from django.db.models import Q
from service_objects.fields import ModelField
from service_objects.services import Service

from models_app.models import User, DirectChat, Message


class DirectChatListService(Service):
    user = ModelField(User)

    def process(self):
        return self.direct_chat_list()

    def direct_chat_list(self):
        direct_chats = DirectChat.objects.filter(
            Q(first_user=self.cleaned_data['user']) |
            Q(second_user=self.cleaned_data['user'])
        )
        interlocutors = []
        for chat in direct_chats:
            interlocutor = chat.first_user if chat.first_user != self.cleaned_data['user'] else chat.second_user
            interlocutor.last_message = Message.objects.filter(direct=chat).order_by('created_at').last()
            interlocutor.direct_chat = chat
            # interlocutor.direct_id = chat.id
            # interlocutor.created_at = chat.created_at
            # interlocutor.hasher_symmetric_key = chat.hasher_symmetric_key
            # interlocutor.l = chat.hasher_symmetric_key
            interlocutors.append(interlocutor)
        return interlocutors
