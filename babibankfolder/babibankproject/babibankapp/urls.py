from django.urls import path


from babibankapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registerin, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('newpage', views.newpage, name="newpage"),
]

