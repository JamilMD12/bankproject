from .models import MyForm
from django import forms
class BankForm(forms.ModelForm):
    class Meta:
        model=MyForm
        fields=['name','dob','age','gender','phoneno','email','address','district','branch']
