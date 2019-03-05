from home import views
from django.urls import path

app_name='home'

urlpatterns = [
    path('add', views.add, name="add"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('add/name/', views.add_name, name="add_name"),
    path('add/number/', views.add_number, name="add_number"),
    path('addsubscriber', views.addsubscriber, name="addsubcriber"),
    path("", views.phonedir, name='phonedir')
]