from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from excursions_markovav_ru_main.forms import AddExcursionForm
from excursions_markovav_ru_main.models import Excursion
from excursions_markovav_ru_main.views.utils import get_base_context


def index_page(request):
    return render(request, 'pages/public/index.html', get_base_context(request))


def excursions_page(request):
    context = get_base_context(request)
    context['excursions'] = Excursion.objects.all()
    return render(request, 'pages/public/excursions.html', context)


@login_required
def add_excursions_page(request):
    name, date, image_link, description = '', '', '', ''
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name', '')
        date = request.POST.get('datetime', '')
        image_link = request.POST.get('image_link', '')
        description = request.POST.get('description', '')
        if name == 'ERROR' or date == 'ERROR' or image_link == '' or description == '':
            messages.add_message(request, messages.ERROR, "Некорректные данные формы")
        try:
            splited_date = date.split(' ', 1)[0].split(':', 1) + date.split(' ', 1)[1].split('.', 2)
            if len(list(map(int, splited_date))) != 5:
                raise ValueError()
        except BaseException:
            messages.add_message(request, messages.ERROR, "Некорректная дата")
        excursion = Excursion(
            name=name,
            datetime=date,
            image_link=image_link,
            free_places=8,
            description=description
        )
        excursion.save()
        messages.add_message(request, messages.SUCCESS, "Экскурсия успешно добавлена")
    context = get_base_context(request)
    context['addexcursionsform'] = AddExcursionForm(initial={'name': name, 'datetime': date, 'image_link': image_link})
    return render(request, 'pages/authorizate/add_excursions.html', context)
