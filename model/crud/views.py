from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddForm, NewsForm
from .models import Person, News


def index(request):
    # makeMen()
    # people = Person.objects.filter(age_gt=17) & Person.objects.filter(name__container='Tom')
    # people = Person.objects.order_by('age','surname')
    # people = Person.objects.values()
    # people = Person.objects.values_list('name',)
    # people = Person.objects.count()
    # people= Person.objects.aggregate(Avg('age'))
    people = Person.objects.all()
    return render(request, 'crud/index.html', context={'people': people})


def create(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            # gender = form.cleaned_data['gender']
            birthDay = form.cleaned_data['birthDay']
            men, _ = Person.objects.get_or_create(name=name, surname=surname, age=age, birthDay=birthDay)
            return redirect('home')
        else:
            form = AddForm()
            return render(request, 'crud/create.html', context={'form': form})

    else:
        form = AddForm()
        return render(request, 'crud/create.html', context={'form': form})


def update(request, id):
    try:
        men = Person.objects.get(id=id)
        if request.method == 'POST':
            men.name = request.POST.get('name')
            men.surname = request.POST.get('surname')
            men.age = request.POST.get('age')
            # men.gender = request.POST.get('gender')

            men.save()
            return redirect('home')
        else:
            return render(request, 'crud/update.html', context={'men': men})
    except:
        return redirect('create')


def delete(request, id):
    try:
        men = Person.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('create')


# автоматически заполняет базу данных makeMen
# def makeMen():
#     m = Person(name='Tom', surname='Tomi', age=18, gender=True, birthDay='2011-12-12')
#     # p = Person.objects.bulk_create(
#     #     [
#     #         m,
#     #         m
#     #     ]
#     # )
#     p, _ = Person.objects.get_or_create(name='Tom', surname='Tomi', age=18, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom1', surname='Tomi', age=19, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom2', surname='Tomi', age=20, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom3', surname='Tomi', age=21, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom4', surname='Tomi', age=22, gender=True, birthDay='2011-12-12')


def news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            is_published = form.cleaned_data['is_published']
            category = form.cleaned_data['category']

            News.objects.create(title=title, content=content, is_published=is_published, category=category)

            return HttpResponse(f"Новость {title}<br>"
                                f"Контект {content}<br>"
                                f"Вид {is_published},{category}")

    else:
        form = NewsForm()

    return render(request, 'crud/news.html', context={'form': form})


# def news_update(request,id):
#     try:
#         news = News.objects.get_(id=id)
#         if request.method == "POST":
#             news.title = request.POST.get('title')
#             news.content = request.POST.get('content')
#             news.is_published = request.POST.get('is_published')
#             news.category = request.POST.get('category')
#             news.save()
#             return redirect
#

