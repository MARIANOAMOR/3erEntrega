from django.urls import path
from AppCoder import views
from AppCoder.views import ContactoListar
from django.contrib.auth.views import LogoutView
urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    #path('profesores', views.profesores, name="Profesores"),
    #path('MostrarCanales', views.formularioMostrarCanal, name="MostrarCanales"),
    #path('app_contactos/', ContactoListar.as_view(template_name = "AppCoder/MostrarCanales.html"), name='MostrarCanales'),
    #path('MostrarCanales', views.CursoDetalle.as_view(), name="MostrarCanales"),
    #path('curso/list', views.CursoList.as_view(), name='List'),
    #path(r'^(?P<pk>\d+)$', views.CursoDetalle.as_view(), name='Detail'),
    #path(r'^nuevo$', views.CursoCreacion.as_view(), name='New'),
    #path(r'^editar/(?P<pk>\d+)$', views.CursoUpdate.as_view(), name='Edit'),
    #path(r'^borrar/(?P<pk>\d+)$', views.CursoDelete.as_view(), name='Delete'),
    ##### Canales
    path('AgregarCanales', views.formularioCargarCanal, name="AgregarCanales"),
    path('MostrarCanales/', views.leerCanal, name="MostrarCanales"),
    path('eliminarCanal/<canal_nombre>/', views.eliminarCanal, name="eliminarCanal"),
    path('editarCanal/<canal_nombre>/', views.editarCanal, name="editarCanal"),
    ##### Productos
    path('AgregarProductos', views.formularioCargarProductos, name="AgregarProductos"),
    path('MostrarProductos/', views.leerProductos, name="MostrarProductos"),
    path('eliminarProductos/<productos_nombre>/', views.eliminarProductos, name="eliminarProductos"),
    path('editarProductos/<productos_nombre>/', views.editarProductos, name="editarProductos"),
    ##### Datos Canal
    path('AgregarDatosCanal', views.formularioDatosCanal, name="AgregarDatosCanal"),
    path('MostrarDatosCanal/', views.leerDatosCanal, name="MostrarDatosCanal"),
    path('eliminarDatosCanal/<DatosCanal_campo1>/', views.eliminarDatosCanal, name="eliminarDatosCanal"),    
    path('editarDatosCanal/<DatosCanal_campo1>/', views.editarDatosCanal, name="editarDatosCanal"),

    path('buscarCanal/', views.buscarCanal),
    #### Login
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    
    ] 

