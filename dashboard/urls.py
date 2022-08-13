from django.urls import path
from . import views
urlpatterns = [
	path('dashboad', views.dashboard, name="dashboard"), 
	path('myprofile', views.profile, name="profile"),   
	path('test_dashboard',views.test_dashboard,name="test")
]
