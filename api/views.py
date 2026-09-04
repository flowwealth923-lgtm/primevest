from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Account


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("password2", "")

        if password != password2:
            return render(request, "signup.html", {"error": "Passwords do not match."})

        if User.objects.filter(username=username).exists():
            return render(request, "signup.html", {"error": "Username already taken."})

        if email and User.objects.filter(email=email).exists():
            return render(request, "signup.html", {"error": "Email already used."})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # ✅ create balance record
        Account.objects.create(user=user)

        # ✅ auto login then go to dashboard
        login(request, user)
        return redirect("dashboard")

    return render(request, "signup.html")


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(username=username, password=password)

        if user is None:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

        login(request, user)
        return redirect("dashboard")

    return render(request, "login.html")


@login_required(login_url="login")
@login_required(login_url="login")
def dashboard_view(request):
    account, _ = Account.objects.get_or_create(user=request.user)
    return render(request, "dashboard.html", {"account": account})

def logout_view(request):
    logout(request)
    return redirect("login")

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def plan(request):
    return render(request, "plan.html")

def deposit(request):
    return render(request, "deposit.html")

