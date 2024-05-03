from django import forms
from . models import Producto, Proveedor



class ProveedorForm(forms.ModelForm ):
    
    
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido', 'dni','telefono','cuit', 'direccion', 'email']

        labels={'nombre':'Nombre del proveedor:',
                 'apellido': 'Apellido del proveedor:', 
                 'dni': 'DNI:',
                 'telefono':'Teléfono:',
                 'cuit':'Cuit:', 
                 'direccion':'Dirección:', 
                 'email':'Email:'}
        widgets ={
                'nombre':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese Nombre'}),
                'apellido':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese Apellido'}),
                'dni':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese el DNI'}),
                'telefono':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ejemplo 3496345678'}),
                'cuit' :forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese Cuit'}),
                'direccion':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese la dirección'}),
                'email':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese el correo electrónico'}) 

                                              
        }
    def clean_dni(self):
        dni = self.cleaned_data.get("dni")
        if len(dni)<8 and dni.isdigit():
            raise forms.ValidationError("El DNI debe contener 8 caracteres")
      
        return dni

    def clean_cuit(self):
        cuit = self.cleaned_data.get('cuit')
        if cuit.isdigit() and len(cuit)==11:
            return cuit
        else:
            raise forms.ValidationError("El cuit de contener solo números y contener 11 dígitios")



class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre', 
            'categoria',
            'stock_actual',
            'precio',
            'proveedor',
        ]

        labels = {
            'nombre':'Nombre del producto', 
            'categoria': 'Seleccione una categoría',
            'stock_actual': 'Cargue el Stock',
            'precio': 'Precio del producto',
            'proveedor': 'Selecciona un Proveedor',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese Nombre del producto'}),
           
            'categoria':forms.Select(attrs={'class':'form-select',
                                            }),
            'stock_actual':forms.NumberInput(attrs={'class':'form-control',
                                                'initial':'ingrese la cantidad'}),
            'precio' :forms.NumberInput(attrs={'class':'form-control',
                                                'placeholder':'Ingrese el precio'}),
            'proveedor':forms.Select(attrs={'class':'form-select',
                                                }),
               
        }