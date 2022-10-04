from django.urls import path
from . import views
urlpatterns = [
    
    path('<int:students_id>', views.showdata , name='detail'),
    path('<int:students_id>/<int:students_subid>/', views.showsubdata , name='subdetail'),
]