from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.views.generic import create_update

from djangodemo.subjecten.models import Subject, SubjectForm
from djangodemo.zaken.models import Zaak, NewZaakForSubjectForm
  
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
	
def zaken(request, subject_id):
	'''Show zaken for this subject'''
	
	zaken = Zaak.objects.filter(subject = subject_id)
	subject = Subject.objects.get(pk = subject_id)
	return render_to_response('subjecten/zaken.html', {'zaken': zaken, 'subject': subject})
	
def new_zaak_for_subject(request, subject_id):
	'''Create new zaak for a subject'''
	
	subject = get_object_or_404(Subject, pk = subject_id)
	
	if request.method == "POST":
		form = NewZaakForSubjectForm(request.POST) #prefilled form from POST data
		if form.is_valid():
			new_zaak = Zaak()
			new_zaak.subject = subject
			for k,v in form.cleaned_data.iteritems():
				setattr(new_zaak, k, v)
			new_zaak.save()
			return HttpResponseRedirect("/subjecten/%s/zaken/" % subject.pk)
	else:
		form = NewZaakForSubjectForm() #empty form
	return render_to_response('subjecten/new_zaak_for_subject.html', {'form': form, 'subject': subject})