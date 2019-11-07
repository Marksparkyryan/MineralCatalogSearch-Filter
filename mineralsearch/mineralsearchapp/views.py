import re

from django.shortcuts import render
from .models import Mineral


def pagination():
    """Finds first letter of each mineral and returns as a unique list
    """
    minerals = Mineral.objects.values(
        'name'
    ).all()
    pagin_set = sorted(set(map(lambda x: x['name'][0].lower(), minerals)))
    pattern = re.compile(r'[a-z]')
    return [x for x in pagin_set if pattern.match(x)]


def index(request):
    """View that displays all mineral objects
    """
    minerals = Mineral.objects.all()
    pagination_list = pagination()
    context = {
        'minerals': minerals,
        'pagination_list': pagination_list,
    }
    return render(request, 'mineralsearchapp/index.html', context)


def detail(request, pk):
    mineral = Mineral.objects.get(id=pk)
    context = {
        'mineral': mineral,
        'pagination_list': pagination(),
    }
    return render(request, 'mineralsearchapp/detail.html', context)


def firstletter(request, letter):
    """View that takes in a letter kwarg and finds all minerals that
    start with that character
    """
    minerals = Mineral.objects.filter(
        name__startswith=letter
    )
    context = {
        'minerals': minerals,
        'pagination_list': pagination(),
    }
    return render(request, 'mineralsearchapp/index.html', context)

def search(request):
    query = request.GET.get('q')
    minerals = Mineral.objects.filter(
        name__icontains=query
    )
    context = {
        'minerals': minerals,
        'pagination_list': pagination(),
        'query': query,
    }
    return render(request, 'mineralsearchapp/index.html', context)

