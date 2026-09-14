from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from solucion import decidir  # Reutiliza tu función original de la ES1
from .models import Registro
from .decorators import requiere_rol


# --- VISTAS DE AUTENTICACIÓN ---
def vista_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username", "").strip(),
            password=request.POST.get("password", "")
        )
        if user:
            login(request, user)
            return redirect("lista")
        messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "login.html")


def vista_logout(request):
    logout(request)
    return redirect("login")


# --- VISTAS CRUD CON SEGURIDAD POR ROLES ---
@login_required(login_url="login")
def lista(request):
    # READ: Filtra registros activos (no eliminados lógicamente)
    registros = Registro.objects.filter(eliminado=False)
    return render(request, "lista.html", {"registros": registros})


@requiere_rol("admin", "normal")
def crear(request):
    # CREATE: Permitido para roles 'admin' y 'normal'
    error = None
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        estado = request.POST.get("estado", "").strip().lower()
        try:
            cantidad = int(request.POST.get("cantidad", ""))
            resultado = decidir(cantidad, estado)  # Aplica regla de decisión
            Registro.objects.create(
                nombre=nombre,
                cantidad=cantidad,
                estado=estado,
                resultado=resultado
            )
            return redirect("lista")
        except ValueError:
            error = "La cantidad debe ser un número entero."

    return render(request, "form.html", {"accion": "Crear", "error": error})


@requiere_rol("admin")
def editar(request, pk):
    # UPDATE: Solo permitido para el rol 'admin'
    reg = get_object_or_404(Registro, pk=pk, eliminado=False)
    error = None
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        estado = request.POST.get("estado", "").strip().lower()
        try:
            cantidad = int(request.POST.get("cantidad", ""))
            reg.nombre = nombre
            reg.cantidad = cantidad
            reg.estado = estado
            reg.resultado = decidir(cantidad, estado)  # Recalcula obligatoriamente la regla
            reg.save()
            return redirect("lista")
        except ValueError:
            error = "La cantidad debe ser un número entero."

    return render(request, "form.html", {"accion": "Editar", "registro": reg, "error": error})


@requiere_rol("admin")
def eliminar(request, pk):
    # DELETE LÓGICO: Solo permitido para el rol 'admin'
    reg = get_object_or_404(Registro, pk=pk, eliminado=False)
    if request.method == "POST":
        reg.soft_delete()  # Oculta el registro usando borrado lógico
        return redirect("lista")
    return render(request, "confirmar.html", {"registro": reg})