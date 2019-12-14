from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('add/', views.add_password, name='add_passwords'),
    path('displaypas/<int:id>', views.display_password, name='display_passwords'),
    path('delete/<int:id>', views.delete_password, name='delete_passwords'),
    path('', views.search_view, name='search_passwords'),

]
