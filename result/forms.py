from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *
from django.views.generic.edit import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'

class CreateStudent(ModelForm):
    class Meta:
        model=Student
        fields=['HallTicketNo','name','dob','age','address','branchName']
        labels={'HallTicketNo':'HALL TICKET NO','name':'NAME','dob':'NAME',
        'age':'AGE','address':'ADDRESS','branchName':'BRANCH'}
        widgets = {
            'region': forms.ChoiceField(
            widget=forms.Select(attrs={'class':'select'})
            ),
            }

        def clean(self):
            fields=self.cleaned_data

sems=(("1-1","1-1"),("1-2","1-2"),("2-1","2-1"),("2-2","2-2"),("3-1","3-1"),("3-2","3-2"),("4-1","4-1"),("4-2","4-2"))

class StudentLoginForm(forms.Form):
    HallTicketNo = forms.CharField(label='Hall Ticket Number', max_length=100)
    sem = forms.ChoiceField(choices=sems, initial='1-2')

class CreateBranch(ModelForm):
    class Meta:
        model=Branches
        fields='__all__'

class CreateSubjects(ModelForm):
    class Meta:
        model=Subjects
        fields='__all__'

class CreateNotice(ModelForm):
    class Meta:
        model=Notices
        fields='__all__'

class CreateSubjectCombination(ModelForm):
    class Meta:
        model=SubjectCombination
        fields='__all__'

class DeclareResults(ModelForm):
    class Meta:
        model=Results
        fields='__all__'

class GettingResult(ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class EditStudent(UpdateView):
    class Meta:
        model=Student
        fields=["HallTicketNo"]

class AddResult(ModelForm):
    class Meta:
        model=Results
        fields='__all__'