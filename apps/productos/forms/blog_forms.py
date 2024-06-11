from django import forms

from ..models.blog_models import Contacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'
        exclude = ('estado',)

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Ingrese su Nombre',
        }
        ),
            'apellido':forms.TextInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Ingrese su Apellido',
        }
        ),
            'correo': forms.EmailInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Ingrese su Correo Electronico',
                }
            ),
            'asunto': forms.TextInput(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Ingrese su asunto',
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'form_control',
                    'placeholder': 'Ingrese su mensaje',
                }
            ),
        }