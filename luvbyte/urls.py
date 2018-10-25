"""luvbyte URL Configuration
"""
from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import logout
from luvbytes import views as luv_views
from account import views as ac_views
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', luv_views.home, name='home'),
    # path('my', luv_views.my_view, name='my'),
    path('logout', luv_views.signout, name="logout"),
    path('setup/', ac_views.SetUp.as_view(), name='setup'),
    path('signup', ac_views.SignUp.as_view(), name='signup'),
    path('login/',auth_views.LoginView.as_view(), name='login'),
    path('admin/statuscheck/', include('celerybeat_status.urls')),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),


]
