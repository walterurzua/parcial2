from django.shortcuts import render
from quesito.models import registro
from quesito.forms import RegistroForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from quesito.models import Productos


# Create your views here.
def inicio (request):
    return render(request, 'inicio.html', {})

def creaciondeusuarios (request):
    return render(request, 'creaciondeusuarios.html', {})

def audifonos (request):
    return render(request, 'audifonos.html', {})

def escritorio (request):
    return render(request, 'escritorio.html', {})

def fuente (request):
    return render(request, 'fuente.html', {})

def monitor (request):
    return render(request, 'monitor.html', {})

def placa (request):
    return render(request, 'placa.html', {})

def lista (request):
    if 'listar' in request.POST: # como filtrar con el ORM
                lista = Productos.objects.all()
    return render(request, 'lista.html', {})

def buscarPorId(modelo, id):
    try:
        item = modelo.objects.get(pk=id)
    except:
        item = {}
    return item

def productos (request):
    mensaje = ""
    lista 	= {}
    item 	= {}
    errores	= {}
    if request.method == "POST":
            id          = int("0" + request.POST["id"])
            nombrep 	= request.POST['nombrep']
            descripcion = request.POST['descripcionp']
            stock 		= request.POST['stockp']
            precioCosto = request.POST['preciocosto']
            precioVenta	= request.POST['precioventa']
            if 'agregar' in request.POST: # validar informacion
                if nombrep == "":
                    mensaje = "Porfavor ingrese Nombre"
                elif descripcion == "":
                    mensaje = "Porfavor ingrese Descripcion"
                elif stock == "":
                    mensaje = "Porfavor ingrese Stock"
                elif precioCosto == "":
                    mensaje = "Porfavor ingrese precio Costo"
                elif precioVenta == "":
                    mensaje = "Porfavor ingrese Precio de Venta"
                elif id < 1:
                    uploaded_file = request.FILES['imagen']
                    fs = FileSystemStorage()
                    Productos.objects.create(nombrep=nombrep,descripcion=descripcion,stock=int(stock),precioCosto=int(precioCosto),precioVenta=int(precioVenta), img=uploaded_file)
                else:
                    item = buscarPorId(productos, id)
                    if not isinstance(item, Productos):
                        mensaje = "No se debe ingresar ID"
                    else:
                        item.nombre = nombrep
                        item.descripcion = descripcion
                        item.stock = stock
                        item.precioCosto = precioCosto
                        item.precioVenta = precioVenta
                        uploaded_file = request.FILES['imagen']
                        fs = FileSystemStorage()
                        item.save()
                        mensaje = "La solicitud fue realizada con éxito"
                    item = {}
            elif 'listar' in request.POST: # como filtrar con el ORM
                lista = Productos.objects.filter(nombrep__contains = nombrep)
            elif 'buscar' in request.POST:
                item = buscarPorId(Productos, id)
                if not isinstance(item, Productos):
                    mensaje = "Registro no encontrado"
            elif 'eliminar' in request.POST:
                item = Productos.objects.get(pk = id)

                if isinstance(item, Productos):
                    item.delete()
                    mensaje = "Registro eliminado"
                    item = {}
    context = {'mensaje' : mensaje, 'lista': lista, 'item': item, 'errores': errores}
    return render(request, 'productos.html', context)

def teclado (request):
    return render(request, 'teclado.html', {})


class RegistroUsuario(CreateView):
    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    success_url = "http://127.0.0.1:8000/"

def listaimg(request):
    productos = Productos.objects.all()
    return render(request,'lista.html',{'producto':productos})


    