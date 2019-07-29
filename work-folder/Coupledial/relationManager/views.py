from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
# Create your views here.
class Homepage(TemplateView):
	#return render(request,'homePage.html', None)
	template_name = 'base.html'


