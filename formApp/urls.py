from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.student_input_view),
    #url for feedback form
    path('feesback/',views.feedback_input_view),
    #url for signup form
    path('singup/',views.signup_form_view),
]
