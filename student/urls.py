from django.urls import path, include
from .views import *

urlpatterns = [
    path('', student, name='student'),
    path('login/', login, name='login'),
    path('login_process/', login_process, name='login_process'),
    path('update_success', update_success, name='update_success'),
    path('edit/<int:id>', edit, name='edit'),
    path('update/<int:id>', update, name='update'),
]