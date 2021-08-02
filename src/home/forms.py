from django import forms
from .models import Complaint, Registraion



class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['Complaint_text',]
    

class RegistraionForm(forms.ModelForm):
    class Meta:
        model = Registraion
        fields = []
    