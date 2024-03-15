from django import forms
from .models import ShareOwnershipModel, SlotModel


class SlotsForm(forms.ModelForm):
    class Meta:
        model = SlotModel
        fields: str = '__all__'
        widgets: dict = {
            'progres_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }


class ShareOwnershipForm(forms.ModelForm):

    class Meta:
        model = ShareOwnershipModel
        exclude: tuple = 'owner', 'slots'
        # read_only_fields: tuple = 'owner', 'slots'
        widgets: dict = {
            'share': forms.Select(attrs={'class': 'form-control'}),
        }


class UpdateShareOwnershipForm(forms.ModelForm):
    class Meta:
        model = ShareOwnershipModel
        exclude: tuple = 'owner', 'slots'
        # read_only_fields: tuple = 'owner', 'slots'
        widgets: dict = {
            'share': forms.Select(attrs={'class': 'form-control disabled', 'disabled': True}),
        }
        read_only_fields: tuple = 'share',
