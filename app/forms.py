from django import forms
from .models import TodoList

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title']


    
class EditTaskForm(forms.ModelForm):
    task_title = forms.CharField()
    class Meta:
        model = TodoList
        fields = ['status']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.title = self.cleaned_data['task_title']
        if commit:
            instance.save()
        return instance