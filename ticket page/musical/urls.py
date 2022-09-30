from django.urls import path
from musical import views

app_name = 'musical'

urlpatterns = [
    path('',views.MusicalLV.as_view(),name='index'),
    path('<int:pk>/',views.MusicalDV.as_view(),name='detail'),
]