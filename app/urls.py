from django.urls import path,re_path
from . import views

app_name='app'
urlpatterns = [
    path("",views.resrurants,name='hello'),
    path("res/<int:id>",views.resturants_detail,name='detail')
]
