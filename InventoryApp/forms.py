from django import forms
from .models import Goods

# class GoodsForm(forms.Form):
#     name=forms.CharField()
#     location=forms.CharField()
#     price=forms.CharField()

class GoodsForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Name of Assets',
        }
    ))
    location=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Location of Assets',
        }
    ))
    price=forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Price of Assets',
        }
    ))
    class Meta:
        model=Goods
        fields='__all__'
    

