from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, Login, Registration
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task_create/', TaskCreate.as_view(), name='task_create'),
    path('task_update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task_delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
]