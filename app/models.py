from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Resume_model(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    about_you_short = models.CharField( max_length=250)
    email = models.EmailField( max_length=254)
    phone = PhoneNumberField(unique= True)
    # place = models.CharField(max_length=254)

    skills = models.CharField(max_length=25) # need more than one
    awards = models.CharField(max_length=250,null=True) # need more than one
    languages = models.CharField( max_length=50) # need more than one
    interests = models.CharField(max_length=50) # need more than one

    #education  
    #more than one
    school_name = models.CharField(max_length=150)
    school_place = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    school_in = models.DateField()
    school_out = models.DateField()

    #experience
    #more than one
    company_name = models.CharField(max_length=150)
    company_place = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    company_in = models.DateField()
    company_out = models.DateField()

    #projects
    #more than one
    project_name = models.CharField(max_length=250)
    project_detail = models.TextField()

    
    def __str__(self):
        return self.name