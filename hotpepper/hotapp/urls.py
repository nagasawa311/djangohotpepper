from django.urls import path
from . import views

urlpatterns = [
	path("",views.first,name="first"),
	path("home",views.home,name="home"),
	path("list",views.list,name="list"),
	path("tonai",views.tonai,name="tonai"),
	path("houdai",views.houdai,name="houdai"),
	path("detail/<item_id>",views.detail,name="detail"),
	path("delete/<id>",views.delete,name="delete"),
	path("signup",views.signup,name="signup"),
	path("login",views.log_in,name="login"),
	path("logout",views.log_out,name="logout"),
	path("loggingout",views.loggingout,name="loggingout")
]
