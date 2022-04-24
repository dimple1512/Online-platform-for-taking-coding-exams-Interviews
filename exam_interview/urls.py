from exam_interview import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.cover,name='cover'),
    path('home',views.home,name='home'),
    path('exam',views.exam,name='exam'),
    path('h',views.greetings),
    path('h/run',views.runcode),
    path('codingsection_completed',views.codingsection_completed,name='codingsection_completed'),
    path('score',views.score,name='score'),
    path('interview',views.interveiw,name='interview'),
    path('about',views.about,name='about'),
    path('contact',views.contactview,name='contact'),
    path('login',views.loginview,name='login'),
    path('register',views.registerview,name='register'),
    path('logout',views.logoutview,name='logout'),
    path('lr',views.lr,name='lr'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]