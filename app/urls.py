from django.urls import path 
from . import views
from django_pdfkit import PDFView


urlpatterns = [
    path("",views.Main_view.as_view(),name="main"),
    # path("resume-builder",views.resume_builder,name="resume-builder"),
    path("resume-builder",views.Resume_builder.as_view(),name="resume-builder"),
    path("detail-resume/<int:id>",views.Resume_detail_view.as_view(),name="detailresume"),
    path("download-pdf",views.GeneratePdf.as_view(),name="to-pdf"),
    path("down-pdf",PDFView.as_view(template_name="detail_resume.html"),name="down-pdf")
]
