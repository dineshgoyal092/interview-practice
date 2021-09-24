from django.urls import path
from . import views

urlpatterns = [
    path('tickets/<int:customer_id>', views.TicketView.as_view()),
    path('ticket/',views.TicketView.as_view()),
    # path('customer_search/',views.CustomerView.as_view())
    
]