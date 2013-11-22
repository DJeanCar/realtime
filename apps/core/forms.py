from django import forms
from .models import Comentario

class ComentariosForm(forms.ModelForm):
	class Meta:
		model = Comentario