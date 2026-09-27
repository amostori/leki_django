from django.shortcuts import render
from .forms import SampleForm
from django_ajax.decorators import ajax
from .symptoms import get_symptoms


def home(request):
	form = SampleForm()
	return render(request, 'home.html', {'form': form})

@ajax
def my_ajax_view(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            return {'status': 'success', 'message': get_symptoms(),}
        else:
            return {'status': 'error', 'errors': form.errors}
