from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import UploadForm
from .models import Upload

# Create your views here.

class UploadView(FormView):
    template_name = 'index.html'
    form_class = UploadForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        print(form.cleaned_data)
        return super().form_valid(form)
