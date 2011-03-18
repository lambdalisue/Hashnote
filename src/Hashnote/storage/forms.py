# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/24
#
from django import forms
from markitup.widgets import MarkItUpTextarea
from models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
             'file', 
        )
class MaterialDescriptionForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
             'file', 'is_public', 'is_downloadable', 'title', 'description',
        )
        widgets = {
            'description': MarkItUpTextarea,
        }
class MaterialDescriptionUpdateForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
             'is_public', 'is_downloadable', 'title', 'description',
        )
        widgets = {
            'description': MarkItUpTextarea,
        }
