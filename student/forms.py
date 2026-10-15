from django import forms
from student.models import Profile


Gender_Choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('S', 'Shemale'),
)


Job_City_choice = [
    ('Alabama', 'Alabama'),
    ('Alaska', 'Alaska'),
    ('Arizona', 'Arizona'),
    ('Arkansas', 'Arkansas'),
    ('California', 'California'),
    ('Colorado', 'Colorado'),
    ('Connecticut', 'Connecticut'),
    ('Delaware', 'Delaware'),
    ('Florida', 'Florida'),
]


class ProfileForm(forms.ModelForm):

    Gender = forms.ChoiceField(
        choices=Gender_Choices,
        widget=forms.RadioSelect
    )

    Job_City = forms.MultipleChoiceField(
        choices=Job_City_choice,
        widget=forms.CheckboxSelectMultiple,
        label='Preferred Job Cities',
        help_text='Select one or more cities to prefer your work'
    )

    class Meta:
        model = Profile

        fields = [
            'Name',
            'Date_Of_Birth',
            'Gender',
            'Locality',
            'City',
            'Pin',
            'Choose_Your_State',
            'Mobile',
            'Email',
            'Job_City',
            'profile_image',
            'my_file'
        ]

        labels = {
            'Name': 'Full Name',
            'Pin': 'Pin Code',
            'Mobile': 'Mobile Number',
        }

        help_texts = {
            'profile_image': 'Optional: Upload a profile image',
            'my_file': 'Optional: Attach any additional Document (PDF, DOCX, etc.)',
        }

        widgets = {
            'Name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'Date_Of_Birth': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'id': 'datepicker',
                    'type': 'date'
                }
            ),

            'Locality': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your area name'
                }
            ),

            'City': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Write your city'
                }
            ),

            'Pin': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter 6-digit code'
                }
            ),

            'Choose_Your_State': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'Mobile': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your mobile number'
                }
            ),

            'Email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your email address'
                }
            ),
        }