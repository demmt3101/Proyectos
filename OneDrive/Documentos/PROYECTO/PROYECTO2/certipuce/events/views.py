from ssl import ALERT_DESCRIPTION_ACCESS_DENIED
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from .models import Events
from .forms import TaskForm


# Create your views here.
def base(request):
    return render(request, "base.html")


def index(request):
    return render(request, "index.html")


def procesar_login(request):
    if request.method == "GET":
        return render(request, "procesar_login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "base.html",
                {
                    "Form": AuthenticationForm,
                    "error": ALERT_DESCRIPTION_ACCESS_DENIED,
                },
            )
        else:
            login(request, user)
            return redirect("pl")


def cerrar_cesion(request):
    logout(request)
    return redirect("index.html")


def crear_usuario(request):
    if request.method == "GET":
        return render(request, "crear_usuario.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                    email=request.POST["email"],
                )
                user.save()
                login(request, user)
                return redirect("pl")
            except IntegrityError:
                return render(
                    request,
                    "crear_usuario.html",
                    {"form": UserCreationForm, "error": "Usuario ya existe"},
                )
        return render(
            request,
            "crear_usuario.html",
            {"form": UserCreationForm, "error": "Contraseña no coincide"},
        )


def crear_evento(request):
    if request.method == "GET":
        return render(request, "crear_evento.html", {"form": TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("ap")
        except ValueError:
            return render(
                request,
                "crear_evento.html",
                {"form": TaskForm, "error": "Error creating task."},
            )


def recuperar_contraseña(request):
    return render(request, "recuperar_contraseña.html")


def index_admin(request):
    return render(request, "index_admin.html")


def cesion_admin(request):
    if request.method == "GET":
        return render(request, "admin_participantes.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "base.html",
                {
                    "Form": AuthenticationForm,
                    "error": ALERT_DESCRIPTION_ACCESS_DENIED,
                },
            )
        else:
            login(request, user)
            return redirect("pl")


def cerrar_admin(request):
    logout(request)
    return redirect("index_admin.html")


def admin_participantes(request):
    return render(request, "admin_participantes.html")


def actualizar_datos(request):
    if request.method == "GET":
        return render(request, "actualizar_datos.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                return HttpResponse("Usuario actaulizado satisfactoriamente")
            except:
                return HttpResponse("Datos Similires")
        return HttpResponse("Contraseñas no coinciden")


def task_detail(request, task_id):
    if request.method == "GET":
        task = get_object_or_404(Events, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, "actualizar_datos.html", {"task": task, "form": form})
    else:
        try:
            task = get_object_or_404(Events, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect("tasks")
        except ValueError:
            return render(
                request,
                "actualizar_datos.html",
                {"task": task, "form": form, "error": "Error updating task."},
            )


def emitir_certificados(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["demmt3101@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silenty=False)
        return render(request, "emision_exitosa.html")
    return render(request, "emitir_certificado.html")
