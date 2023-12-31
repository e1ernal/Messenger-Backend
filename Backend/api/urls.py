from django.urls import path

from conf.yasg import urlpatterns as docs_urls
from api.views import *

urlpatterns = [
    # Codes
    path('verification_codes/', VerificationCodeCreateView.as_view()),
    path('verification_codes/confirm/', VerificationCodeConfirmView.as_view()),

    # Users
    path('users/', UserCreateView.as_view()),
    path('users/username/', UserUsernameCheckView.as_view()),
    path('users/me/', UserMeDetailView.as_view())
]

urlpatterns += docs_urls
