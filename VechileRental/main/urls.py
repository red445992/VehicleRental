from django.urls import path
from .views import *

urlpatterns = [
    # Home
    path('',home, name="home"),

    # Customer-related routes
    path('previous_rentals/', previous_rentals, name="previous_rentals"),
    path('current_orders/', current_orders, name="current_orders"),

    # Authentication
    path('register/', register, name="register"),
    path('login/', log_in, name="log_in"),
    path('logout/', log_out, name="log_out"),


    path('showdetails/',showdetails,name="showdetails"),
    path('order/',order,name = "order"),


    path('update/<int:id>',update,name="update"),
    path('delete/<int:ida>',delete_data,name="delete_data"),
]
