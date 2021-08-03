from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect # agrega redirección a la declaración de importación

# Create your views here.
def root(request):
	return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")    

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, numblog):
    return HttpResponse(f"placeholder para mostrar el blog numero : {numblog}")

def edit(request, numblog):
    return HttpResponse(f"placeholder para editar el blog : {numblog}")

def destroy(request, numblog):
    return redirect("/blogs")