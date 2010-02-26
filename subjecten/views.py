from django.shortcuts import render_to_response

from djangodemo.subjecten.models import Subject

def index(request):
	'''Lijst van alle subjecten'''
	
	subjecten = Subject.objects.all()
	return render_to_response('subjecten/index.html', {'subjecten': subjecten})
    
def detail(request, subject_id):
	'''Details van een subject'''
	
	subject = Subject.objects.get(pk = subject_id)
	return render_to_response('subjecten/detail.html', {'subject': subject})
  