from django import forms
from apps.inicio.models.inicio_principal_models import Banner, Servicio, Testimonio, Equipo

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = '__all__'

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
