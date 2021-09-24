from django.urls import path, include
from . import views

app_name = "booking"

urlpatterns = [
    path('movie/', views.MovieView.as_view()),
    path('movie/<pk>', views.MovieView.as_view()),
    path('show/', views.ShowView.as_view()),
    path('shows/<int:pk>', views.ShowView.as_view()),
    path('shows/', views.ShowView.as_view()),
    path('seats/<int:show_id>', views.SeatView.as_view()),
    # path('shows/<int:movie_id>', views.ShowView.as_view()),
    # path('shows/<int:movie_id>/<int:theater_id>', views.ShowView.as_view()),
    # path('shows/<int:movie_id>/<int:theater_id>/<str:date>', views.ShowView.as_view()),
    # path('shows/', views.get_shows, name='get_shows'),
]