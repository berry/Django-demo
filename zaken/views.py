from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from djangodemo.zaken.models import Zaak, NewZaakForSubjectForm

# vooralsnog leeg... ik kan tot nu toe alles met generic views doen! Zie urls.py

def edit(request, zaak_id):
	'''Edit existing zaak. You are not allowed to change subject 
	attributes for an existing zaak.'''
	
	# I am reusing NewZaakForSubjectForm because it contains the fields
	# you are allowed to edit.
	
	zaak = get_object_or_404(Zaak, pk = zaak_id)
		
	if request.method == "POST":
		form = NewZaakForSubjectForm(request.POST) #prefilled form from POST data
		if form.is_valid():
			for k,v in form.cleaned_data.iteritems():
				setattr(zaak, k, v)
			zaak.save()
			return HttpResponseRedirect("/subjecten/%s/zaken/" % zaak.subject.pk)
	else:
		form = NewZaakForSubjectForm(initial={'type_zaak': zaak.type_zaak, 'opmerkingen': zaak.opmerkingen}) #empty form
	return render_to_response('zaken/edit_zaak.html', {'form': form, 'zaak': zaak})
