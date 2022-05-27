from django.shortcuts import render, redirect
from .models import Url
import random, string
from django.contrib import messages

def getAlias():
    return "".join([random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(8)])

def dashboard(request):
    if request.method == "POST":
        URL = request.POST["URL"]
        alias = request.POST.get("alias", None)
        if not alias:
            alias = getAlias
        try:
            Url.objects.create(user=request.user, target_url=URL, alias=alias).save()
            messages.success(request, "shorted successfully")
            return redirect("dashboard")
        except:
            messages.error(request, "Alias already in used.")
            return render(request, "dashboard.html", {"url": URL, "alias": alias})
    return render(request, 'dashboard.html')
