from home import views
from django.urls import path

app_name='home'

urlpatterns = [
    path('add', views.add, name="add"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('addsubscriber', views.addsubscriber, name="addsubcriber"),
    path("", views.phonedir, name='phonedir')
]