# from django.shortcuts import render, redirect
# from .models import Author
# from .forms import AuthorForm, ImageForm
#
#
# # Create your views here.
#
# def get_cabinet(request):
#     authors = Author.objects.all().order_by('id')
#     print(locals())
#     return render(request, 'cabinet.html', locals())
#
#
# def detail_cabinet(request, id):
#     author = Author.objects.get(id=id)
#     return render(request, 'detail_cabinet.html', locals())
#
#
# def create_author(request):
#     forms=AuthorForm()
#     if request.method == 'POST':
#         forms = AuthorForm(request.POST)
#     # print(request.POST)
#         if forms.is_valid():
#             # query = request.POST.pop('csrfmiddlewaretoken')
#             sur_name = request.POST.get('sur_name')
#             name = request.POST.get('name')
#             username = request.POST.get('username')
#             Author.objects.create(sur_name=sur_name,
#                                   name=name,
#                                   username=username,
#                                   )
#             return redirect('main')
#             # print(request.POST)
#     return render(request, 'create.html', locals())
#
# def create_image(request):
#     forms = ImageForm()
#     if request.method == 'POST':
#
#         forms = ImageForm(request.POST, request.FILES, instance = request.user)
#         # print(request.POST)
#         if forms.is_valid():
#
#             forms.save()
#             return redirect ('main')
#     return render(request, 'create_image.html', locals())
#
# def update_author(request, id):
#     Author.objects.filter(id=id).first()
#     form = AuthorForm(request.POST or None, instance=Author)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     return render(request, 'update.html', locals())

from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm, ImageForm


def get_cabinet(request):
    sur_name=request.GET.get('sur_name', None)
    authors = Author.objects.all().order_by('id')
    if sur_name:
        authors = Author.objects.filter(sur_name__icontains=sur_name).order_by('id')


    print(request)
    return render(request, 'cabinet.html', locals())


def detail_cabinet(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'detail_cabinet.html', locals())


def create_author(request):
    forms = AuthorForm()
    if request.method == 'POST':
        forms = AuthorForm(request.POST)
        if forms.is_valid():
            sur_name = request.POST['sur_name']
            name = request.POST['name']
            username = request.POST.get('username')

            Author.objects.create(sur_name=sur_name,
                                  name=name,
                                  username=username,

                                  )
            return redirect('main')
    return render(request, 'create.html', locals())

def create_image(request):
    forms = ImageForm()
    if request.method == 'POST':
        forms = ImageForm(request.POST, request.FILES)
        print(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('main')
    return render(request, 'create_image.html', locals())


def update_author(request, id):
    author = Author.objects.filter(id=id).first()
    form = AuthorForm(request.POST or None, instance=author)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, 'update.html', locals())

def delete_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        author.delete()
        return redirect('main')
    return render(request, 'delete.html', locals())