from django import forms

class FormularioEstudiante(forms.Form):
    
    nombre = forms.ChoiceField(required=True,max_length=100)