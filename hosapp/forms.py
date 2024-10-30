from django import forms
from .models import Patient
from .models import Doctor
class DataForm(forms.ModelForm):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    DOCTOR_CHOICES = [('Dr.Aparna', 'Dr.Aparna'), ('Dr.Archana', 'Dr.Archana'), ('Dr.Amal', 'Dr.Amal')]
   

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    mobile = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    disease = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    doctor = forms.ChoiceField(choices=DOCTOR_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
   
    class Meta:
        model = Patient
        fields = ['name', 'age', 'mobile', 'gender', 'disease', 'doctor']





class DataFormNew(forms.ModelForm):
    Dr_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Patient_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    profile = forms.FileInput()
   
  
    class Meta:
        model = Doctor
        fields = ['Dr_name','Patient_name','profile']
