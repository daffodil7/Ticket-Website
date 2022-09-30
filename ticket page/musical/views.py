from django.views.generic import ListView, DetailView
from .models import Musical


class MusicalLV(ListView):
    model = Musical

class MusicalDV(DetailView):
    model = Musical
