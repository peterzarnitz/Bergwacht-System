from django import forms
from .fields import DateTimePickerField
from .models import Takes_part_in_duty


class Duty_signup_form(forms.ModelForm):
    class Meta:
        model = Takes_part_in_duty
        exclude = ['duty', 'member', ]
        field_classes = {
            'from_time': DateTimePickerField,
            'to_time': DateTimePickerField,
        }

    def __init__(self, *args, **kwargs):
        super(Duty_signup_form, self).__init__(*args, **kwargs)