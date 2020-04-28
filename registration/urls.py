
from django.urls import path, include 

from . import views

app_name = 'registration'


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

]