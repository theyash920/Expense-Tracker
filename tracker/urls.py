#urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login_view,name='login_view'),
    path('register/',views.register_view,name='register_view'),
    path('logout/',views.logout_view,name='logout_view'),
    path('',views.index,name='index'),
     path('delete-transaction/<id>/', views.delete_transaction , name="delete_transaction"),
]