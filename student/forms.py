from django import forms
from .models import StudentRegister


class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = StudentRegister
        fields = "__all__"
