from django.conf.urls import url


from . import views


app_name = 'notes'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.userLogin, name='login'),
	url(r'^newLogin/$', views.userNewLogin, name='new_login'),
	url(r'^signup/$', views.userSignup, name='signup'),
	url(r'^newSignup/$', views.userNewSignup, name='new_signup'),
	url(r'^@(?P<user_name>\w+)/logout/$', views.userLogout, name='logout'),
	url(r'^@(?P<user_name>\w+)/dashboard/$', views.userDashboard, name='dashboard'),
	url(r'^@(?P<user_name>\w+)/user_profile/$', views.userProfile, name='user_profile'),
	url(r'^@(?P<user_name>\w+)/add_note/$', views.addNote, name='add_note'),
	url(r'^@(?P<user_name>\w+)/add_new_note/$', views.addNewNote, name='add_new_note'),
	url(r'^zapier_input',views.hook_receiver_view,name='add_new_note'),

]