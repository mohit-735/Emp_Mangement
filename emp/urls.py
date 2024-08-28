# from django.contrib import admin
from django.urls import path
from .views import emp_home, add_emp, delete_emp, update_emp, do_update_emp
from .views import testimonials
# from django.conf.urls.static import static

urlpatterns = [
   path("home/", emp_home),
   path("add-emp/", add_emp),
   path("delete-emp/<int:emp_id>", delete_emp),
   path("update-emp/<int:emp_id>", update_emp),
   path("do-update-emp/<int:emp_id>", do_update_emp),
   path("testimonials/", testimonials, name='testimonials'),
] 
