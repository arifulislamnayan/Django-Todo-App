from django.shortcuts import render
from django.http import HttpResponse
from models import Todo
from django.shortcuts import render_to_response
from django.views.generic import CreateView




class CreateView(CreateView):
	template_name ='core/create.html'
	model = Todo
	success_url = '/core/'



def index(request):
	items = Todo.objects.all()

	return render_to_response('core/index.html', {'items': items}) 
	


