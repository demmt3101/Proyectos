from django.forms import ModelForm
from .models import Events


class TaskForm(ModelForm):
    class Meta:
        model = Events
        fields = ["nombre", "fecha", "lugar", "hora"]
