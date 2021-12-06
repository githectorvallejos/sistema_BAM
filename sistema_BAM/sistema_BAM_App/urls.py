from django.urls import path
from sistema_BAM_App import views

urlpatterns = [
    path('',views.home, name='home'),
    
]
