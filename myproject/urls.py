from myapp import views 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list),
    path('students/<int:pk>', views.students),
]
