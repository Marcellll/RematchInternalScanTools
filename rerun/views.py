from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import OrdreFabrication, Rerun, PeseeProduction
from .forms import RerunForms
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def RerunList(request: HttpRequest) -> HttpResponse:
    open_ordre = OrdreFabrication.objects.filter(status_of='Planifié').select_related('id_lot')
    return render(request, 'rerun/open_order_list.html', {'open_ordre': open_ordre})

@login_required(login_url='/login')
def RerunDetailList(request: HttpRequest, id_of) -> HttpResponse:
    if request.method == 'GET':
        Rerun.objects.filter(id_ordre_fabrication_rerun=id_of).select_related()
        return render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': Rerun.objects.filter(id_ordre_fabrication_rerun=id_of).select_related()})
    
    if request.method == 'POST':
        form = RerunForms(request.POST)
        try:
            numero_pesee = form.data['numero_pesee']
            pesee = PeseeProduction.objects.get(numero_pesee=numero_pesee)
        except Exception as e:
            messages.error(request, f"Pesée {numero_pesee} n'existe pas")
            return render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': Rerun.objects.filter(id_ordre_fabrication_rerun=id_of).select_related()})

        if Rerun.objects.filter(id_pesee_production=pesee).exists():
            messages.error(request, f"Pesée {numero_pesee} est déjà dans le Re-run")
            return render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': Rerun.objects.filter(id_ordre_fabrication_rerun=id_of).select_related()})

        of = OrdreFabrication.objects.get(pk=id_of)
        Rerun.objects.create(id_ordre_fabrication_rerun=of, id_pesee_production=pesee)
        messages.success(request, f"Pesée {numero_pesee} ajoutée au Re-run")
        return redirect('re_run_order', id_of=id_of)#render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': Rerun.objects.filter(id_ordre_fabrication_rerun=id_of).select_related()})
    
@login_required(login_url='/login')
def DeleteRerun(request: HttpRequest, id_pesee) -> HttpResponse:
    pesee_rerun = Rerun.objects.get(pk=id_pesee)
    pesee_rerun.delete()
    messages.error(request, f"Pesée {pesee_rerun.id_pesee_production.numero_pesee} a été supprimé du Rerun")
    return redirect('re_run_order', id_of=pesee_rerun.id_ordre_fabrication_rerun)
#render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': Rerun.objects.filter(id_ordre_fabrication_rerun=pesee_rerun.id_ordre_fabrication_rerun).select_related()})

#class ReRunView(ListView):
#    model = Lot
#    template_name = 'rerun/open_order_list.html'
#    context_object_name = 'open_ordre'
#    queryset = OrdreFabrication.objects.filter(status_of='Planifié').select_related('id_lot')


#class ReRunDetailView(ListView):
#    model = OrdreFabrication
#    template_name = 'rerun/re_run_order.html'
#    context_object_name = 'rerun'

#    @login_required(login_url='/login/')
#    def get(self, request, *args, **kwargs):        
#        return render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': self.get_queryset()}) 
    
#    def post(self, request, *args, **kwargs):
#        print("in post")
#        form = RerunForms(request.POST)
#        if form.is_valid():
#            rerun = form.save(commit=False)
#            rerun.id_ordre_fabrication_rerun = OrdreFabrication.objects.get(pk=self.kwargs['of_id'])
#            print(rerun)
#            rerun.save()
        
#        return render(request, 'rerun/re_run_order.html', {'form': RerunForms(), 'rerun': self.get_queryset()})

    
#    def get_queryset(self):
#        of_id = self.kwargs['of_id']
#        return Rerun.objects.filter(id_ordre_fabrication_rerun=of_id
#                                    ).select_related()
    
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['ordre_fabrication'] = OrdreFabrication.objects.get(pk=self.kwargs['of_id'])
#        return context
    
#    def get_absolute_url(self):
#        return reverse('re_run_order', args=[str(self.id)])
    


