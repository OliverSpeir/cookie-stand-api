from django.urls import path
from .frontend_views import (
    CookieStandCreateView,
    CookieStandDetailView,
    CookieStandDeleteView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path('', CookieStandListView.as_view(), name='list'),
    path('<int:pk>/', CookieStandDetailView.as_view(), name='detail'),
    path('create/', CookieStandCreateView.as_view(), name='create'),
    path('<int:pk>/update/', CookieStandUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CookieStandDeleteView.as_view(), name='delete')
]