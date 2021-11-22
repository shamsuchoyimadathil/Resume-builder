from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,DetailView,View
from django.urls import reverse
from .utils import render_to_pdf



from .forms import ResumeFormSet
from .models import Resume_model 
# Create your views here.

class Main_view(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    

def resume_builder(request):
    context = {}
    formset = ResumeFormSet(queryset=Resume_model.objects.none())
    if request.method == "POST":
        formset = ResumeFormSet(request.POST)
        context["form"] = formset
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('detailresume',args=(formset.instance.id,)))
        return render(request,"resume-builder.html",context)
    context["form"] = formset
    context["a"] = 238

    return render(request,"resume-builder.html",context)
    
class Resume_detail_view(DetailView):
    template_name = "detail_resume.html"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Resume_model,id=id_)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        
        datas = {
            
        }

        pdf = render_to_pdf('detail_resume.html',datas)
        return HttpResponse(pdf, content_type='application/pdf') 
