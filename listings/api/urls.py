from django.urls import path
from .views import ListingsRudView, ListingsAPIView

urlpatterns = [
    path('', ListingsAPIView.as_view(), name='post-create'),
    path('<int:pk>/', ListingsRudView.as_view(), name='post-rud'),
]
