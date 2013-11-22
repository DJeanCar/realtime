from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Comentario
from .forms import ComentariosForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json

class IndexView(TemplateView):

	def get(self, request, *args, **kwargs):
		return render(request, 'core/index.html')


class LibroView(TemplateView):

	def get(self, request, *args, **kwargs):
		comentarios = Comentario.objects.all()
		comentarios_form = ComentariosForm()
		dic = {'comentarios':comentarios, 'comentarios_form':comentarios_form}
		return render(request, 'core/libro.html' , dic)


@csrf_exempt
def NuevoComentario(request):
	if request.method == 'POST':
		print "es get"
		print request.GET.get()
		comentario = Comentario()
		comentario.autor = request.GET.get['autor']
		comentario.comentario = request.GET.get['comentario']
		comentario.save()
		print "guardo"		
		response = {'autor':comentario.autor, 'comentario':comentario.comentario}
		return HttpResponse(json.dumps(response) , mimetype='application/json')
		
	else :
		pass