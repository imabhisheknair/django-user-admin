from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('signup', views.signup),
    path('logout', views.logout),
    path('changepass', views.changep),
    path('admin/', views.admin),
    path('admin/view', views.view),
    path('admin/save', views.save),
    path('admin/delete', views.delete),
    path('admin/block', views.block),
    path('admin/logout', views.adminlogout),
    path('admin/search', views.search),
    path('admin/create', views.create)
]