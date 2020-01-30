from django.shortcuts import render,redirect
import requests
import json
from .models import List,User
from .forms import ListForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# eb63878483aac2f6344afc940a49f120 this is the api key



def first(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		return render(request,"first.html",{})

@login_required
def home(request):
	
	return render(request,"home.html",{})

@login_required
def detail(request,item_id):
	if request.method=="POST":
		area_code=request.POST['area_code']
		api_request=requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=eb63878483aac2f6344afc940a49f120&id=" +item_id)
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api="Error..."
		return render(request,"detail.html",{
			"api":api,
			"area_code":area_code,
		})
	else:
		api_request=requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=eb63878483aac2f6344afc940a49f120&id=" +item_id)
		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api="Error..."
		return render(request,"detail.html",{"api":api,})


@login_required
def list(request):
	if request.method=="POST":
		form=ListForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("list")
	else:
		item_id=List.objects.all()
		output=[]
		for item in item_id:
			api_request=requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=eb63878483aac2f6344afc940a49f120&id=" +str(item))
			try:
				api=json.loads(api_request.content)
				output.append(api)
			except Exception as e:
				api="Error..."

		return render(request,"list.html",{"output":output})

@login_required
def tonai(request):
	api_request=requests.get("https://api.gnavi.co.jp/master/GAreaMiddleSearchAPI/v3/?keyid=eb63878483aac2f6344afc940a49f120&lang=ja")

	try:
		api=json.loads(api_request.content)
	except Exception as e:
		api="Error..."

	return render(request,"tonai.html",{"api":api})



@login_required
def houdai(request):

	if request.method == "POST":
		area_code=request.POST['area_code']
		api_request=requests.get("https://api.gnavi.co.jp/RestSearchAPI/v3/?keyid=eb63878483aac2f6344afc940a49f120&areacode_m=" +area_code+ "&buffet=1")

		try:
			api=json.loads(api_request.content)
		except Exception as e:
			api="Error..."

		return render(request,"houdai.html",{"api":api,"area_code":area_code})

	else:
		return render(request,"houdai.html",{})

@login_required
def delete(request,id):
	list=List.objects.get(item_id=id).delete()
	return redirect("list")


def signup(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			username=request.POST["username"]
			password=request.POST["password"]
			user = User.objects.create_user(username, '', password)
			user.save
			return redirect("home")

		else:
			return render(request,"signup.html",{})

def log_in(request):
	if request.user.is_authenticated:
		return redirect("home")
	else:
		if request.method == "POST":
			username=request.POST["username"]
			password=request.POST["password"]
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request,user)
				return redirect("home")
			else:
				return render(request,"login.html",{"error":"username 又は password が間違っています。"})
		
		else:
			return render(request,"login.html",{})

@login_required
def log_out(request):
	return render(request,"logout.html",{})

@login_required
def loggingout(request):
	logout(request)
	return redirect("first")
	
	