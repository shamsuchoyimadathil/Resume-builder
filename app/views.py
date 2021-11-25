from django.shortcuts import get_object_or_404, redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView,DetailView,View
from django.urls import reverse
from .utils import render_to_pdf
from django.template.loader import get_template


from .forms import ResumeFormSet
from .models import Resume_model 
# Create your views here.

class Main_view(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    

# def resume_builder(request):
#     context = {}
#     formset = ResumeFormSet(queryset=Resume_model.objects.none())
#     if request.method == "POST":
#         formset = ResumeFormSet(data=request.POST,queryset=Resume_model.objects.none())
#         context["form"] = formset

#         if formset.is_valid():
#             print("valid")
#             formset.save(commit=False)
#             return HttpResponseRedirect(reverse('detailresume',args=(formset.instance.id,)))
#         print(formset.non_form_errors())
#         print(formset.errors)
       
#     context["form"] = formset
#     return render(request,"resume-builder.html",context)
    
    
class Resume_builder(TemplateView):
    template_name = "resume-builder.html"

    def get(self, *args, **kwargs):
        formset = ResumeFormSet(queryset=Resume_model.objects.none())
        return self.render_to_response({'resume_formset': formset})

    def post(self,request, *args, **kwargs):
        context = self.get_context_data()
        formset = ResumeFormSet(request.POST)

        if formset.is_valid():
            print("valid")
            formset = formset.save()
            form_id = formset[0].pk
            return HttpResponseRedirect(reverse('detailresume',args=([form_id])))
            
        formset = ResumeFormSet(queryset=Resume_model.objects.none())
        print(formset.errors)
        return super(TemplateView,self).render_to_response(context)


class Resume_detail_view(DetailView):
    template_name = "detail_resume.html"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Resume_model,id=id_)



class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        id_ = self.kwargs.get('id')
        obj = Resume_model.objects.get(id=id_)
        datas = {
            "object":obj
        }

        pdf = render_to_pdf('detail_resume.html',datas)
        return HttpResponse(pdf, content_type='application/pdf') 
