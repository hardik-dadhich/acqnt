from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def homepage(request):
	return render(request,'homePage.html', None)


