from django.shortcuts import render,redirect, HttpResponse
from AppCoder.models import Canal,Productos,DatosCanal
# Create your views here.
def inicio(request):
      return render(request, "AppCoder/inicio.html")
################# login #################################
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})           
        else:
            return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})


from AppCoder.forms import  UserRegisterForm #CursoFormulario, ProfesorFormulario,
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

from django.contrib.auth.decorators import login_required
@login_required
def inicio(request):

    return render(request, "AppCoder/inicio.html")

#@login_required
#def estudiantes(request):

    #return render(request, "AppCoder/estudiantes.html")
############################################################
from AppCoder.forms import canalFormulario
def formularioCargarCanal(request):
      if request.method == "POST":
            miFormulario = canalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  canal = Canal(nombre=informacion['nombre'], descripcion=informacion['descripcion'],
                        campo1=informacion['campo1'], campo2=informacion['campo2'],
                        campo3=informacion['campo3'], campo4=informacion['campo4'],
                        campo5=informacion['campo6'], campo6=informacion['campo6'],
                        campo7=informacion['campo7'], campo8=informacion['campo8'])
                  canal.save()
                  return redirect("AgregarCanales") 
                  #return render(request, "AppCoder/canales.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario = canalFormulario()
      return render(request, "AppCoder/AgregarCanales.html", {"miFormulario": miFormulario})

def formularioMostrarCanal(request, sensor_identificacion):
    canal = Canal.objects.all()  # trae todos los sensores
    contexto = {"canal": canal}
    return render(request, "AppCoder/MostrarCanales.html", contexto)

def eliminarCanal(request, canal_nombre):
    canal = Canal.objects.get(nombre=canal_nombre)
    canal.delete()
    """ # vuelvo al menú
    canal2 = Canal.objects.all()  # trae todos los sensores
    contexto = {"canal": canal2}
    #return render(request, "AppCoder/MostraCanales.html", contexto) """
    return redirect("MostrarCanales")

def leerCanal(request):
      canal = Canal.objects.all() #trae todos los sensores
      contexto= {"canal":canal} 
      return render(request, "AppCoder/MostrarCanales.html",contexto)

def editarCanal(request, canal_nombre):
    # Recibe el nombre del sensor que vamos a modificar
    canal= Canal.objects.get(nombre=canal_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = canalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            canal.nombre = informacion['nombre']
            canal.descripcion = informacion['descripcion']
            canal.campo1 = informacion['campo1']  
            canal.campo2 = informacion['campo2'] 
            canal.campo3 = informacion['campo3'] 
            canal.campo4 = informacion['campo4'] 
            canal.campo5 = informacion['campo5'] 
            canal.campo6 = informacion['campo6'] 
            canal.campo7 = informacion['campo7'] 
            canal.campo8 = informacion['campo8'] 
            canal.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = canalFormulario(initial={'nombre':canal.nombre, 'descripcion':canal.descripcion,
                                                   'campo1':canal.campo1,'campo2':canal.campo2,'campo3':canal.campo3,
                                                   'campo4':canal.campo4,'campo5':canal.campo5,'campo6':canal.campo6,
                                                   'campo7':canal.campo7,'campo8':canal.campo8})
    # Voy al html que me permite editar
    return render(request, "AppCoder/editarCanal.html", {"miFormulario": miFormulario, "nombre": canal_nombre})
"""
def buscar(request):
      if  request.GET["nombre"]:
	      #respuesta = f"Estoy buscando el modelo nro: {request.GET['modelo'] }" 
            nombre = request.GET["nombre"] 
            canal3 = Canal.objects.filter(nombre__icontains=nombre)
            return render(request, "AppCoder/inicio.html", {"canal3":canal3, "nombre":nombre})          
      else: 
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta) 
"""
def buscarCanal(request):
      nombre =request.GET["nombre"]
      if nombre != "" :
            canal = Canal.objects.filter(nombre__icontains=nombre) #(modelo__icontains=modelo)
            return render(request, "AppCoder/inicio.html", {"buscarcanal":canal, "nombre":nombre})#{"sensoresmodelo":sensores, "Modelo":modelo})
      else: 
            respuesta = "No enviaste datos"
      #No olvidar from django.http import HttpResponse
            return HttpResponse(respuesta)
#sensores       canal           
#identificacion nombre
#modelo         descripcion   
#valor          canal1
#               canal2
############  PRODUCTOS #############
from AppCoder.forms import ProductosFormulario
def formularioCargarProductos(request):
      if request.method == "POST":
            miFormulario = ProductosFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  productos = Productos(nombre=informacion['nombre'], descripcion=informacion['descripcion'],
                        precio=informacion['precio'])
                  productos.save()
                  return redirect("AgregarProductos")                   
      else:
            miFormulario = ProductosFormulario()
      return render(request, "AppCoder/AgregarProductos.html", {"miFormulario": miFormulario})

def leerProductos(request):
      productos = Productos.objects.all() #trae todos los sensores
      contexto= {"productos":productos} 
      return render(request, "AppCoder/MostrarProductos.html",contexto)

def eliminarProductos(request, productos_nombre):
    productos = Productos.objects.get(nombre=productos_nombre)
    productos.delete()
    return redirect("MostrarProductos")

def editarProductos(request, productos_nombre):
    # Recibe el nombre del sensor que vamos a modificar
    productos= Productos.objects.get(nombre=productos_nombre)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = ProductosFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            productos.nombre = informacion['nombre']
            productos.descripcion = informacion['descripcion']
            productos.precio = informacion['precio']  
            productos.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProductosFormulario(initial={'nombre':productos.nombre, 'descripcion':productos.descripcion,
                                                   'precio':productos.precio})
    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProductos.html", {"miFormulario": miFormulario, "nombre": productos_nombre})

############  DATOS CANAL #############
from AppCoder.forms import DatosCanalFormulario
def formularioDatosCanal(request):
      if request.method == "POST":
            miFormulario = DatosCanalFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  datosCanal = DatosCanal(campo1=informacion['campo1'], campo2=informacion['campo2'],
                        campo3=informacion['campo3'], campo4=informacion['campo4'],
                        campo5=informacion['campo5'], campo6=informacion['campo6'],
                        campo7=informacion['campo7'], campo8=informacion['campo8'])
                  datosCanal.save()
                  return redirect("AgregarDatosCanal")                   
      else:
            miFormulario = DatosCanalFormulario()
      return render(request, "AppCoder/AgregarDatosCanal.html", {"miFormulario": miFormulario})

def leerDatosCanal(request):
      datoscanal = DatosCanal.objects.all() #trae todos los sensores
      contexto= {"datosCanal":datoscanal} 
      return render(request, "AppCoder/MostrarDatosCanal.html",contexto)

def eliminarDatosCanal(request, DatosCanal_campo1):
    datosCanal = DatosCanal.objects.get(campo1=DatosCanal_campo1)
    datosCanal.delete()
    return redirect("MostrarDatosCanal")

def editarDatosCanal(request, DatosCanal_campo1):
    # Recibe el nombre del sensor que vamos a modificar
    datosCanal= DatosCanal.objects.get(campo1=DatosCanal_campo1)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = DatosCanalFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            datosCanal.campo1 = informacion['campo1']
            datosCanal.campo2 = informacion['campo2']
            datosCanal.campo3 = informacion['campo3']  
            datosCanal.campo4 = informacion['campo4']
            datosCanal.campo5 = informacion['campo5']
            datosCanal.campo6 = informacion['campo6']  
            datosCanal.campo7 = informacion['campo7']
            datosCanal.campo8 = informacion['campo8']
            datosCanal.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = DatosCanalFormulario(initial={'campo1':datosCanal.campo1, 'campo2':datosCanal.campo2,
                                                   'campo3':datosCanal.campo3, 'campo4':datosCanal.campo4,
                                                   'campo5':datosCanal.campo6,'campo6':datosCanal.campo6,
                                                   'campo7':datosCanal.campo7,'campo8':datosCanal.campo8})
    # Voy al html que me permite editar
    return render(request, "AppCoder/editarDatosCanal.html", {"miFormulario": miFormulario, "campo1": DatosCanal_campo1})

#def formularioMostrarCanal(request, canalblock_id=2):
    #canalBlock_name = Canal.objects.get(nombre=canalblock_id)
    #canals_description = list(Canal.objects.filter(canals_canalblock_id=canalblock_id))
    #context = {
    #    "nombre": canalBlock_name, 
    #    "descripcion":canals_description,
    #    "campo1": canalBlock_name1, 
    #    "campo2": canals_description2,
    #    "campo3": canalBlock_name, 
    #    "campo4": canals_description,
    #    "campo5": canalBlock_name, 
    #    "campo6": canals_description,
    #    "campo7": canalBlock_name, 
    #    "campo8": canals_description

    #}
    #return render_to_response('MostrarCanales.html', context)

#Para obtener todos los registros de la tabla Canal 
from django.views.generic import ListView
class ContactoListar(ListView): 
    model = Canal


def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre) # Recibe el nombre del profesor que vamos a modificar  
    if request.method == 'POST': # Si es metodo POST hago lo mismo que el agregar
        # aquí mellega toda la información del html
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']
            profesor.save()
            # Vuelvo al inicio o a donde quieran
            return render(request, "AppCoder/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido,
                                                   'email': profesor.email, 'profesion': profesor.profesion})
    # Voy al html que me permite editar
    return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

from django.views.generic import ListView
class CursoList(ListView):
    model = Canal
    template_name = "AppCoder/cursos_list.html"

from django.views.generic.detail import DetailView
class CursoDetalle(DetailView):
    model = Canal
    template_name = "AppCoder/curso_detalle.html"
    
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CursoCreacion(CreateView):
    model = Canal
    success_url = "/AppCoder/curso_list.html"#/.html
    fields = ['nombre', 'descripcion','campo1','campo2','campo3','campo4','campo5','campo6','campo7','campo8']

from django.views.generic.edit import UpdateView
class CursoUpdate(UpdateView):
    model = Canal
    success_url = "AppCoder/cursos_list.html"#"/AppCoder/curso/list"
    fields = ['nombre', 'descripcion','campo1','campo2','campo3','campo4','campo5','campo6','campo7','campo8']

from django.views.generic.edit import DeleteView
class CursoDelete(DeleteView):
    model = Canal
    success_url = "AppCoder/cursos_list.html"#"/AppCoder/curso/list"