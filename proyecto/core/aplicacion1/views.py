from django.shortcuts import render, redirect
from django.views.generic import ListView
from core.aplicacion1.models import *
from core.aplicacion1.formularioVender import formventa
from core.aplicacion1.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import model_to_dict
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.

@login_required(login_url='/login')
def form_sell(request):

    if request.method == 'POST':

        miformulario = formventa(request.POST, files=request.FILES)

        if miformulario.is_valid():

            info = miformulario.cleaned_data

            username = request.user
            img = request.FILES['imagen']
            img_name = img.name

            upimage(img, str(username), img_name)

            productos.objects.create(nombre=info['nombre'],
                                     seccion=info['seccion'],
                                     precio=info['precio'],
                                     imagen=img_name,
                                     stock=info['stock'],
                                     vendedor=username)

            return redirect('/main')

    else:

        miformulario = formventa()

    return render(request, 'new.html', {'form':miformulario})

def upimage(file_image, user, image_name):

    ruta = 'C:/Users/Rosangel/PycharmProjects/ejemploDjango/proyecto/static/imagenes/perfiles'
    rutaUser = ruta + '/' + user + '/'

    if not os.path.exists(rutaUser):
        os.makedirs(rutaUser)

    fs = FileSystemStorage()
    fs.save(rutaUser + image_name, file_image)


class carrito(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = ordenes
    template_name = 'car.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        #a = ordenes.objects.filter(comprador=self.request.user) #.values('producto')
        #b = productos.objects.filter(pk__in=a)

        pr = []
        monto = 0
        for i in ordenes.objects.filter(comprador=self.request.user):
            producto = productos.objects.get(pk=i.producto_id)
            pr.append([producto, i])
            monto = monto + (int(producto.precio) * int(i.cantidad))

        iva = round(monto*0.12, 2)

        context['car'] = pr
        context['total'] = monto
        context['iva'] = iva
        context['totaliva'] = round(iva + monto, 2)

        return context

@login_required(login_url='/login')
def eliminarCar(request, id):
    ordenes.objects.filter(comprador=request.user, id=id).delete()
    return redirect('/main/car')


@login_required(login_url='/login')
def pruebas(request):
    #ordenes.objects.filter(comprador=request.user, id=id).delete()
    return redirect('/main')
