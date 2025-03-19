from django import forms
from .models import Incident


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'incident_category', 'incident_description', 'incident_location', 'incident_image']

        widgets = {
            'incident_type': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder': 'Incident title'}),
            'incident_location': forms.TextInput(attrs={'class': 'form-control form-control-lg form-control-solid', 'placeholder': 'Location of the incident'}),
            'incident_description': forms.Textarea(attrs={'class': 'form-control form-control-solid', 'placeholder': 'Description', 'rows': 3}),
            'incident_image': forms.ClearableFileInput(attrs={'class': 'form-control card h-100 w-100 flex-center bg-light-primary border-primary border border-dashed p-8' }),
            'incident_category': forms.Select(attrs={'class': 'form-select form-select-solid form-select-lg fw-bold','data-control':'select2'}),
        }