from django.urls import path,include
from website.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]