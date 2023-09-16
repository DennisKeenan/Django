from django.urls import path
from . import views

urlpatterns = [
    path('members/',views.members,name='Members'),
    path('members/detail/<int:id>',views.details,name="Details"),
    path('',views.main,name="Homepage"),
]