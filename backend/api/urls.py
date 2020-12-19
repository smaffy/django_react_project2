from django.urls import path

from . import views


urlpatterns = [
    path('csrf/', views.get_csrf, name='api-csrf'),
    path('login/', views.login_view, name='api-login'),         # allows the user to log in by providing their username and password
    path('logout/', views.logout_view, name='api-logout'),      # logs the user out
    path('session/', views.SessionView.as_view(), name='api-session'),   # checks whether a session exists
    path('whoami/', views.WhoAmIView.as_view(), name='api-whoami'),      # fetches user data for an authenticated user

]
