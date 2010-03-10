from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from djangodemo.subjecten.models import Subject, SubjectForm

def index(request):
	'''Lijst van alle subjecten'''
	
	subjecten = Subject.objects.all()
	return render_to_response('subjecten/index.html', {'subjecten': subjecten})
    
def detail(request, subject_id):
	'''Details van een subject'''
	
	subject = Subject.objects.get(pk = subject_id)
	return render_to_response('subjecten/detail.html', {'subject': subject})
  
def new(request):
	'''Show form to add new subject'''
	
	if request.method == "POST":
		form = SubjectForm(request.POST) #prefilled form from POST data
		if form.is_valid():
			new_subject = form.save()
			return HttpResponseRedirect("/subjecten/%s/" % new_subject.pk)
	else:
		form = SubjectForm() #empty form
	return render_to_response('subjecten/new_subject.html', {'form': form})
	
def edit(request, subject_id = None):
	'''Show form to change an existing subject'''
	
	if request.method == "POST":
		subject = Subject.objects.get(pk = subject_id)
		form = SubjectForm(request.POST, instance = subject)
		if form.is_valid():
			new_subject = form.save()
			return HttpResponseRedirect("/subjecten/%s/" % new_subject.pk)
	else:
		subject = Subject.objects.get(pk = subject_id)
		form = SubjectForm(instance = subject)
	return render_to_response('subjecten/edit_subject.html', {'form': form, 'subject': subject})