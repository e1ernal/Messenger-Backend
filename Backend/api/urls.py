from django.urls import path

from api.views.messages import MessageListCreateView
from conf.yasg import urlpatterns as docs_urls
from api.views import (VerificationCodeCreateView, VerificationCodeConfirmView, UserCreateView,
                       UserUsernameCheckView, UserMeDetailView, UserSearchView, UserUpdateView,
                       DirectChatCreateView, DirectChatDeleteView, DirectChatListView, UserDeleteView, HomePageRenderView)

urlpatterns = [
    # Codes
    path('verification_codes/', VerificationCodeCreateView.as_view()),
    path('verification_codes/confirm/', VerificationCodeConfirmView.as_view()),

    # Users
    path('users/', UserCreateView.as_view()),
    path('users/search/', UserSearchView.as_view()),
    path('users/username/', UserUsernameCheckView.as_view()),
    path('users/me/', UserMeDetailView.as_view()),
    path('users/update/', UserUpdateView.as_view()),
    path('users/<int:id>/direct_chats/', DirectChatCreateView.as_view()),
    path('users/delete/', UserDeleteView.as_view()),

    # Direct chats
    path('direct_chats/', DirectChatListView.as_view()),
    path('direct_chats/<int:id>/', DirectChatDeleteView.as_view()),
    path('direct_chats/<int:id>/messages/', MessageListCreateView.as_view()),

    # Tests
    path('<int:pk>/', HomePageRenderView.as_view())
]

urlpatterns += docs_urls
