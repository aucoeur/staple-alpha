from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from staple.models import Document
from staple.forms import DocumentForm
# Create your views here.

def index(request):
  text = 'I LIKE FOOD IS POTATOE.'
  return render(request, 'staple/index.html', {'text': text})

# class IndexView(generic.ListView):
#     template_name = 'staple/index.html'

# @login_required
# def new_packet(request):
#     return render(request, 'new_packet.html')

class DocumentNewView(CreateView):
  """ Renders a Create New Page Form """
  # login_url = '/accounts/login'
  template_name = 'staple/new_packet.html'
  form_class = DocumentForm
  success_url = '' 

  def get(self, request):
    form = DocumentForm()
    return render(request, 'staple/new_packet.html', {'form': form})

  def post(self, request):
    if request.method == 'POST':
      form = DocumentForm(data=request.POST)
      if form.is_valid():
        article = form.save()
        return HttpResponseRedirect(reverse_lazy('document-details-page', args = [article.slug]))
      return render(request, 'staple/new_packet.html', {'form': form})

class DocumentUpdateView(UpdateView):
  ''' Renders an Edit Document Form'''
  model = Document
  template_name = 'staple/document_edit.html'
  form_class = DocumentForm
  
  def get_success_url(self):
      return reverse('document-details-page', kwargs={
          'slug': self.object.slug,
      })

class DocumentListView(ListView):
  '''Renders list of all documents'''
  model = Document

  def get(self, request):
    '''GET list of documents'''
    documents = Document.objects.filter().order_by('title')
    return render(request, 'staple/list.html', { 'documents': documents })

class DocumentDetailView(DetailView):
  """ Renders a specific page based on its slug."""
  model = Document

  def get(self, request, slug):
      """ Returns a specific wiki page by slug. """
      document = self.get_queryset().get(slug__iexact=slug)
      return render(request, 'staple/document.html', {
        'document': document
      })