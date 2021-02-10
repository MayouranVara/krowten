# -*- coding: utf-8 -*-

from django import forms
from .models import Profile

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('prenom','nomdefamille','description_poste','avatar')