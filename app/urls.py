from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tarefas.views import tasks_view







urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', tasks_view,),

]
