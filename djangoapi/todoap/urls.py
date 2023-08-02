"""djangoapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('',views.apiOverView,name="api-overview"),
    path('task-list/<int:pk>',views.taskList,name="taskList"),
    path('task-create/',views.taskCreate,name="taskCreate"),
    path('task-update/<str:pk>/',views.taskUpdate,name="taskUpdate"),
    path('task-delete/<str:pk>/',views.taskDelete,name="taskDelete"),

    path('task-detail/<str:pk>/',views.taskDetail,name="taskDetail"),

    # Auth

    path('login/',views.Login,name="Login"),
    path('signup/',views.signUp,name="signup"),
]
