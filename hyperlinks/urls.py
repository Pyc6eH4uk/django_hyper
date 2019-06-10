from django.urls import path
from hyperlinks import views

urlpatterns = [
    path('', views.index),
    path('subject/<int:subject_id>', views.object_info, name='object_info')
]
