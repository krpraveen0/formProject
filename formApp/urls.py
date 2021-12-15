from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.student_input_view),
    #url for feedback form
    #url for signup form
]
