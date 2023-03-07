from django import forms
from projects.models import Project


class CreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
        )
