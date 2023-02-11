from django.urls import path
from .api_views import CookieStandAPIList, CookieStandAPIDetail
from .frontend_views import (
    CookieStandCreateView,
    CookieStandDetailView,
    CookieStandDeleteView,
    CookieStandListView,
    CookieStandUpdateView,
)

urlpatterns = [
    path('', CookieStandAPIList.as_view(), name='list_api'),
    path('<int:pk>/', CookieStandAPIDetail.as_view(), name='detail_api'),
]
