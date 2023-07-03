from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import*
from hitcount.views import HitCountDetailView
# Create your views here.
def home (request):
    campos = Campos.objects.all()
    context_object_name = 'campo'
    mais_lidas = Campos.objects.all().order_by('-visualizacoes')
        
    return render(request,"home.html",locals())




def materia (request):
    materias = Campos.objects.all()
    
    return render(request,"materia.html",locals())
    
class HomeView(DetailView):
    model = Campos
    template_name = 'home.html'
    context_object_name = 'campo'


class MateriaView(HitCountDetailView):
    model = Campos
    template_name = 'materia.html'
    count_hit = True
    def get_object(self):
        obj = super().get_object()
        obj.visualizacoes += 1
        obj.save()
        return obj
    def get_context_data(self, *args, **kwargs):
        context = super(MateriaView, self).get_context_data(*args, **kwargs)
        context['campo_list'] = Campos.objects.all()
        context['campo_list_views'] = Campos.objects.all().order_by('-visualizacoes')
        
        return context
      
    
    


    