from django.shortcuts import render
from receitas.models import Receita
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_titulo = Receita.objects.all().count()

    context = {
        'num_titulo': num_titulo,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class ReceitaListView(generic.ListView):
    model = Receita


class ReceitaDetailView(generic.DetailView):
    model = Receita