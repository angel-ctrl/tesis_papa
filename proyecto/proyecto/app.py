from django.shortcuts import render, redirect
from django.http import HttpResponse
from proyecto.formUser import UserRegisterFrom
from core.aplicacion1.models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from datetime import datetime

def inicio(request):

    return render(request, 'index2.html')

def register(request):

    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/main')
    else:
        form = UserRegisterFrom()

    contex = {'form': form}
    return render(request, 'signup.html', contex)

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('/')

class main(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = productos
    template_name = 'profile.html'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):

        if self.request.POST:
            date_insert = self.request.POST.get('search')
            return productos.objects.filter(nombre__icontains=date_insert)
        else:
            return productos.objects.all()

    def get_context_data(self, **kwargs):

        context = super(main, self).get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

@login_required(login_url='/login')
def addcar(request, id):
    username = request.user
    cantidad = request.POST.get('quantity', False)
    texthash = datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + str(cantidad) + str(username)

    ordenes.objects.create(comprador=username,
                           cantidad=cantidad,
                           producto_id=id,
                           code_hash=hash(texthash))
    return redirect('/main/car')