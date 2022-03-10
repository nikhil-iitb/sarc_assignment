from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Student(UserCreationForm):
    def __str__(self):
        return self.name

    name = forms.CharField(max_length=50)
    rollno = forms.CharField(max_length=11)
    mobile = forms.CharField(max_length=11)
    department = forms.CharField(max_length=50)
    degree =forms.CharField(max_length=15)
    subsystem = forms.CharField(max_length=30)
    system = forms.CharField(max_length=20)
    experience = forms.IntegerField()
    topic = forms.CharField(max_length=100)
    about = forms.CharField(max_length=500)
    image = forms.CharField(max_length=300)
    reg_date = forms.DateTimeField()

    class Meta:
        model = User
        fields = ('username','name','rollno','mobile','department','degree','subsystem','system','experience','topic','about','image')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    