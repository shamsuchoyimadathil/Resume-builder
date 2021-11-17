from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,DetailView,View
from django.urls import reverse
from .utils import render_to_pdf



from .forms import Resume_form
from .models import Resume_model 
# Create your views here.

class Main_view(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    

class Resume_builder(TemplateView):
    template_name = "resume-builder.html"
   

    def post(self,request,**kwargs):
        context = self.get_context_data()

        form = Resume_form()
        if request.method == 'POST':
            form = Resume_form(request.POST)
            if form.is_valid():
                form.save()
                
                return HttpResponseRedirect(reverse('detailresume',args=(form.instance.id,)))
        return super(TemplateView,self).render_to_response(context)

        
    def get_context_data(self, **kwargs):
        context = super(Resume_builder,self).get_context_data(**kwargs)
        form = Resume_form(self.request.POST or None)
        context["form"] = form
        return context
    
class Resume_detail_view(DetailView):
    template_name = "detail_resume.html"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Resume_model,id=id_)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('detail_resume.html')
        return HttpResponse(pdf, content_type='application/pdf') 
