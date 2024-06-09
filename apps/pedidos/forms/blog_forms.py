from django import forms
from apps.pedidos.models.blog_pedido_model import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model= Contacto
        fields= '__all__'
        excluide={'estado',}

        widgets={
            'nombre':forms.TextInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'Ingrese su nombre',
                }    
            ),
            'apellido':forms.TextInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'Ingrese su apellido',
                }    
            ),
            'correo':forms.EmailInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'Ingrese su correo electronico',
                }    
            ),
            'asunto':forms.TextInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'Ingrese el asunto',
                }    
            ),
            'mensaje':forms.TextInput(
                attrs={
                 'class':'form-control',
                 'placeholder':'Ingrese su mensaje',
                }    
            ),
        }