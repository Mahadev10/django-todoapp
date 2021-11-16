from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
        else:
            return render(request, "users/user_signup.html", context={"signup_form": form})
    else:
        form = UserCreationForm()
        return render(request, "users/user_signup.html", context={"signup_form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user=user)
            return redirect("home")
    else:
        form = AuthenticationForm()
        return render(request, "users/user_login.html", context={"login_form": form})


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
    else:
        return redirect("login")
