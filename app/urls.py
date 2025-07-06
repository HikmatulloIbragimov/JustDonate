from django.urls import path
from .views import BalanceApi, UpdateUserApi, SendVerifyApi
from transaction.views import CreateTransactionApi


urlpatterns = [
    path('balance/', BalanceApi.as_view()),
    path('update-user/', UpdateUserApi.as_view()),
    path('verify/', SendVerifyApi.as_view()),
    path('buy/', CreateTransactionApi.as_view()),
]
