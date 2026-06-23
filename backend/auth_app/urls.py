from django.urls import path, include

from auth_app.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
