from django.urls import path
from .views import user_login, user_join, user_logout

urlpatterns = [
    path('login/', user_login),
    path('registration/', user_join),
    path('logout/', user_logout),
]