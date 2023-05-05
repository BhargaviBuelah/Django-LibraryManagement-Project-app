from django.urls import path
from libraryapp import views

urlpatterns = [
   path('main',views.main),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.edit),
   path('sort/<sv>',views.sort),
   path('sortname/<sn>',views.sortname),
   path('filter/<vcat>',views.filter),
   path('register',views.register),
   path('login',views.user_login),
   path('logout',views.user_logout),
  
]
