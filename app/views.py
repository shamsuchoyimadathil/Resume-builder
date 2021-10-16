from django.views.generic import TemplateView
# Create your views here.

class Main_view(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["a"] = "working..."
        return context
    
    

class Resume_builder(TemplateView):
    template_name = "resume-builder.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["b"] = "working............"
        return context
    
    
