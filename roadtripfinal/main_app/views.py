from django.db.models import query
from django.views.generic import View, ListView, CreateView, DetailView, DeleteView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Roadtrips, Stays

# Create your views here.

class roadtrip(ListView):
    def get(self, request):
        queryset = Roadtrips.objects.all()
        context = {
            "objects": queryset
        }
        return render (request,'roadtrips/roadtrip_list.html', context)

class stays(ListView):
    def get(self, request):
        queryset = Stays.objects.all()
        context = {
            "objects": queryset
        }
        return render (request,'stays/stay_list.html', context)

def home(request):
    return render(request, 'home.html')

def roadtrip_detail(request, id):
    object = get_object_or_404(Roadtrips, id=id)
    context = {
        'object': object
    }
    return render(request, 'roadtrips/roadtrip_detail.html', context)
    
def stay_detail(request, id):
    object = get_object_or_404(Stays, id=id)
    context = {
        'object': object
    }
    return render(request, 'stays/stay_detail.html', context)
    
def about(request):
    return render(request, 'about.html')

class roadtrip_create(CreateView):
    model = Roadtrips
    fields = '__all__'
    success_url = '/roadtrip/'

class stay_create(CreateView):
    model = Stays
    fields = '__all__'
    template_name = 'stays/stay_update.html'
    success_url = '/stay/'

class roadtrip_update(UpdateView):
    model = Roadtrips
    fields = '__all__'
    template_name = 'roadtrips/roadtrip_update.html'
    success_url = '/roadtrip/'

class stay_update(UpdateView):
    model = Stays
    fields = '__all__'
    template_name = 'stays/stay_update.html'
    success_url = '/stay/'

class roadtrip_delete(DeleteView):
    model = Roadtrips
    context_object_name = 'roadtrips'
    template_name = 'roadtrips/roadtrip_delete.html'
    success_url = '/roadtrip/'

class stay_delete(DeleteView):
    model = Stays
    context_object_name = 'stays'
    template_name = 'stays/stay_delete.html'
    success_url = '/stay/'