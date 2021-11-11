from django import forms
from django.forms import fields
from . import models
class NoteModelForm(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ('title','due_date','label')