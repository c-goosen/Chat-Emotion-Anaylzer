# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from myproject.myapp import EmotionAnalysis

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
import os


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])

            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    #Viewing the graph
    # for document in documents:
        # EmotionAnalysis.printgraph(document.docfile.name)


    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )
