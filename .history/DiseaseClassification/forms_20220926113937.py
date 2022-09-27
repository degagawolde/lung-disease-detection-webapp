from pyexpat import model
from django.forms import ModelForm
from .models import Diagnosis

class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        exclude = ["diagnosis","confidence"]