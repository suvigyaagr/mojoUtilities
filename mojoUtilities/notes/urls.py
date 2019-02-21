from django.conf.urls import url


from . import views


app_name = 'notes'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^@(?P<user_name>\w+)/dashboard/$', views.userDashboard, name='dashboard'),

]