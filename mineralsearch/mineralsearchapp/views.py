import re

from django.shortcuts import render
from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()

    # pagination logic
    pagin_set = sorted(set(map(lambda x: x.name[0].lower(), minerals)))
    pattern = re.compile(r'[a-z]')
    valid_pagin_list = [x for x in pagin_set if pattern.match(x)]

    context = {
        'minerals': minerals,
        'pagin_list': valid_pagin_list,
    }

    return render(request, 'mineralsearchapp/index.html', context)

def detail(request):
    pass

def firstletter(request, letter):
    allminerals = Mineral.objects.all()
    filteredminerals = Mineral.objects.filter(
        name__startswith=letter
    )

    # pagination logic
    pagin_set = sorted(set(map(lambda x: x.name[0].lower(), allminerals)))
    pattern = re.compile(r'[a-z]')
    valid_pagin_list = [x for x in pagin_set if pattern.match(x)]

    context = {
        'minerals': filteredminerals,
        'pagin_list': valid_pagin_list,
    }

    return render(request, 'mineralsearchapp/index.html', context)
