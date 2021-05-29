from django.shortcuts import render

from excursions_markovav_ru_main.views.utils import get_base_context


def index_page(request):
    return render(request, 'pages/public/index.html', get_base_context(request))


def excursions_page(request):
    return render(request, 'pages/public/excursions.html', get_base_context(request))
