from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views
app_name = 'main_app'

urlpatterns = [
    path('block', BlockView.as_view()),
    path('exhibition', ExhibitionView.as_view()),
    path('ticket', TicketView.as_view()),
    path('ticket-status', ticketStatusChanger),
]
