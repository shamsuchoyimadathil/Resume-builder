from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,DetailView
from django.urls import reverse

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
                clean_data = form.cleaned_data
                data = Resume_model(name=clean_data['name'],profession=clean_data['profession'],about_you_short=clean_data['about_you_short'],
                                    email=clean_data['email'],phone=clean_data['phone'],skills=clean_data['skills'],awards=clean_data['awards'],
                                    languages=clean_data['languages'],interests=clean_data['interests'],school_name=clean_data['school_name'],
                                    school_place=clean_data['school_place'],qualification=clean_data['qualification'],school_in=clean_data['school_in'],
                                    school_out=clean_data['school_out'],company_name=clean_data['company_name'],company_place=clean_data['company_place'],
                                    position=clean_data['position'],company_in=clean_data['company_in'],company_out=clean_data['company_out'],project_name=clean_data['project_name'],
                                    project_detail=clean_data['project_detail'],)
                data.save()
                print(id)
                return HttpResponseRedirect(reverse('detailresume',args=(id,)))
                # return redirect('detailresume',id)
           
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
