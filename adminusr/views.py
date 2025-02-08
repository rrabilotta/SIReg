from django.shortcuts import render
from .forms import form_CrearUsuarioInterno
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_usuarioInterno(request):
    if request.method == "GET":
        return render(request, "register.html", {"form": form_CrearUsuarioInterno},)
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"]
                )
                user.save()
                login(request, user)
            except IntegrityError:
                return render(
                    request,
                    "register.html",
                    {
                        "form": form_CrearUsuarioInterno,
                        "error": "Nombre de usuario ya existente en nuestro registro",
                    },
                )
        else:
            return render(
                request,
                "register.html",
                {
                    "form": form_CrearUsuarioInterno,
                    "error": "Las contraseñas no coinciden",
                },
            )


@login_required
def logOut(request):
    logout(request)
    return redirect("home")


def LogIn(request):
    if request.user.is_authenticated==False:
        if request.method == "GET":
            return render(request, "login.html", {"form": AuthenticationForm})
        else:
            user = authenticate(
                request, username=request.POST["username"], password=request.POST["password"]
            )
            if user is None:
                return render(
                    request,
                    "login.html",
                    {"form": AuthenticationForm, "error": "Los datos son erróneos"},
                )
            else:
                login(request, user)
                return redirect("home")
    else:
       return render(
                    request,
                    "login.html",
                    {"form": AuthenticationForm, "error": "Debe terminar con la sesión primeramente"},
       )