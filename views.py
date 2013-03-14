from pdfs.models import PDF
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    return render_to_response('pdf_index.html', 
        {'editions': PDF.objects.order_by('issue')},
        context_instance=RequestContext(request),
    )

