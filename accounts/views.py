from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        if username and password:
            user = auth.authenticate(request, username=username, password=password)
            if user:
                auth.login(request,user)
                messages.success(request, "Login success")
                return render(request, "home.html")
            messages.error(request, "Incorrect credentials")
            return render(request, "login.html", {"username":username})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        email = request.POST.get("email", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)
        if password2 == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)
            except:
                messages.error(request, "User with this Username, Already exist!")
                return render(request, "register.html", {"username": username, "email": email})

            messages.success(request, "user creation successful")
            return redirect("/")
    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("login")
