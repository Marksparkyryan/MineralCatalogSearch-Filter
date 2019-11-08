import re

from django.shortcuts import render

from .forms import MineralSearchForm
from .models import Mineral


GROUPS = [
    'Silicates',
    'Oxides',
    'Sulfates',
    'Sulfides',
    'Carbonates',
    'Halides',
    'Sulfosalts',
    'Phosphates',
    'Borates',
    'Organic Minerals',
    'Arsenates',
    'Native Elements',
    'Other',
]

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def detail(request, pk):
    mineral = Mineral.objects.get(id=pk)
    context = {
        'mineral': mineral,
        'pagination_list': ALPHABET,
        'form': MineralSearchForm(),
        'groups': GROUPS,
    }
    return render(request, 'mineralsearchapp/detail.html', context)


def letter(request, letter='a'):
    """View that takes in a letter kwarg and finds all minerals that
    start with that character
    """
    minerals = Mineral.objects.values(
        'name',
        'pk'
    ).filter(
        name__startswith=letter
    )
    form = MineralSearchForm()
    context = {
        'minerals': minerals,
        'pagination_list': ALPHABET,
        'form': form,
        'groups': GROUPS,
        'alphaquery': letter,
    }
    return render(request, 'mineralsearchapp/index.html', context)

def search(request):
    """View that accepts q query from the MineralSearchForm and filters
    mineral names on that query
    """
    if request.method == 'GET':
        form = MineralSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            minerals = Mineral.objects.values(
                'name',
                'pk'
            ).filter(
                name__icontains=query
            )
            context = {
                'minerals': minerals,
                'pagination_list': ALPHABET,
                'form': form,
                'groups': GROUPS,
            }
            return render(request, 'mineralsearchapp/index.html', context)
    minerals = Mineral.objects.values(
        'name',
        'pk'
    ).all(),
    context = {
            'minerals': minerals,
            'pagination_list': ALPHABET,
            'form': form,
            'groups': GROUPS,
        }
    return render(request, 'mineralsearchapp/index.html', context)


def group(request, group):
    minerals = Mineral.objects.values(
        'name',
        'pk'
    ).filter(
        group__icontains=group
    )
    context = {
        'minerals': minerals,
        'pagination_list': ALPHABET,
        'form': MineralSearchForm(),
        'groups': GROUPS,
        'groupquery': group,
    }
    return render(request, 'mineralsearchapp/index.html', context)

