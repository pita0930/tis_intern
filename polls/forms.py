from django.forms import ModelForm
from django import forms
from .models import Event
from .models import Comment
from .models import User

class EventForm(ModelForm):

    class Meta:
        model = Event
        fields = ('event_name', 'place', 'help', 'parttime', 'join', 'planning_number', 'thanks', 'user')


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment',
            'user',
        ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs['value'] = '名無し'

