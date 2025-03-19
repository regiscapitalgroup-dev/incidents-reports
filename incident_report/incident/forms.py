from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'incident_category', 'incident_description', 'incident_location', 'incident_client', 'incident_image']

        widgets = {
            'incident_type': forms.Select(attrs={'class': 'form-select form-select-solid form-select-lg fw-bold','data-control':'select2'}),
            'incident_location': forms.Select(attrs={'class': 'form-select form-select-solid form-select-lg fw-bold','data-control':'select2'}),
            'incident_description': forms.Textarea(attrs={'class': 'form-control form-control-solid', 'placeholder': 'Description', 'rows': 3}),
            'incident_client': forms.Select(attrs={'class': 'form-select form-select-solid form-select-lg fw-bold','data-control':'select2'}),
            'incident_category': forms.Select(attrs={'class': 'form-select form-select-solid form-select-lg fw-bold','data-control':'select2'}),
            'incident_image': forms.ClearableFileInput(attrs={'class': 'form-control card h-100 w-100 flex-center bg-light-primary border-primary border border-dashed p-8' }),
            
        }