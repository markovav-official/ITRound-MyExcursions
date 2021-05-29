import hashlib

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from excursions_markovav_ru_main.forms import AddExcursionForm
from excursions_markovav_ru_main.models import Excursion
from excursions_markovav_ru_main.views import bilet_generator
from excursions_markovav_ru_main.views.utils import get_base_context


def index_page(request):
    return render(request, 'pages/public/index.html', get_base_context(request))


def excursions_page(request):
    if request.method == 'GET' and request.GET.get('jointo', 'ERROR') != 'ERROR':
        bilet = request.GET.get('jointo')
        excursion = Excursion.objects.get(name_date__exact=bilet)
        if excursion is not None and excursion.free_places > 0:
            excursion.free_places -= 1
            excursion.save()
            return bilet_generator.generate(excursion.name, excursion.datetime, excursion.to_qr())
    if request.method == 'GET' and request.user.is_authenticated and request.GET.get('delete', 'ERROR') != 'ERROR':
        bilet = request.GET.get('delete')
        excursion = Excursion.objects.get(name_date__exact=bilet)
        if excursion is not None:
            excursion.free_places -= 1
            excursion.delete()
    context = get_base_context(request)
    rows = []
    for item in list(Excursion.objects.all()):
        if len(rows) == 0 or len(rows[-1]) >= 3:
            rows.append([item])
        else:
            rows[-1].append(item)
    context['excursions'] = rows
    return render(request, 'pages/public/excursions.html', context)


@login_required
def add_excursions_page(request):
    name, date, image_link, description = '', '', '', ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        date = request.POST.get('datetime', '')
        image_link = request.POST.get('image_link', '')
        description = request.POST.get('description', '')
        if name == 'ERROR' or date == 'ERROR' or image_link == '' or description == '':
            messages.add_message(request, messages.ERROR, "Некорректные данные формы")
        elif len(Excursion.objects.filter(name_date__exact=hashlib.md5(str(name + date).encode('utf-8')).hexdigest())) != 0:
            messages.add_message(request, messages.ERROR, "Экскурсия уже существует")
        else:
            try:
                splited_date = date.split(' ', 1)[0].split(':', 1) + date.split(' ', 1)[1].split('.', 2)
                if len(list(map(int, splited_date))) != 5:
                    raise ValueError()
            except BaseException:
                messages.add_message(request, messages.ERROR, "Некорректная дата")
            else:
                excursion = Excursion(
                    name_date=hashlib.md5(str(name + date).encode('utf-8')).hexdigest(),
                    name=name,
                    datetime=date,
                    image_link=image_link,
                    free_places=8,
                    description=description
                )
                excursion.save()
                messages.add_message(request, messages.SUCCESS, "Экскурсия успешно добавлена")
    context = get_base_context(request)
    form_initial = {'name': name, 'datetime': date, 'image_link': image_link, 'description': description}
    context['addexcursionsform'] = AddExcursionForm(initial=form_initial)
    return render(request, 'pages/authorizate/add_excursions.html', context)
