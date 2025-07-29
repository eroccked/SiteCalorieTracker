from django import forms
from .models import UserProfile  # Імпортуємо нашу модель UserProfile


class UserProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = UserProfile
        fields = [
            'height',
            'weight',
            'desired_weight',
            'gender',
            'date_of_birth',
            'activity_level',
            'allergies',
            'profile_picture',
        ]
        labels = {
            'height': 'Зріст (см)',
            'weight': 'Вага (кг)',
            'desired_weight': 'Бажана вага (кг)',
            'profile_picture': 'Фото профілю',
            'gender': 'Стать',
            'date_of_birth': 'Дата народження',
            'activity_level': 'Рівень активності',
            'allergies': 'Алергії',
        }
        widgets = {
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'desired_weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'activity_level': forms.Select(attrs={'class': 'form-select'}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
