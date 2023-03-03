from django.urls import path
from .import views

urlpatterns = [
  
    path('',views.index,name="index"),
    path('view-emp/',views.view_emp,name="view-emp"),
    path('add-emp/',views.add_emp,name="add-emp"),
    path('filter-emp/',views.filter_emp,name="filter-emp"),
    path('delete-emp/',views.delete_emp,name="delete-emp"),
    path('delete-emp/<int:emp_id>',views.delete_emp,name="delete-emp")

]
