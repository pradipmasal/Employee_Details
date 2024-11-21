
from django.urls import path

from employee import views


urlpatterns = [
    path('new_employee/',views.new_employee,name='new_employee'),
    path('employees',views.employees,name='employees'),
    path('<int:pk>/',views.employee_details,name='employee_details'),
]