from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import BlogForm
from .models import BlogModel


def home(request):
    data = BlogModel.objects.all()

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()

    context = {
        'form': form,
        'data': data
    }
    return render(request, 'core/home.html', context)


def read_one(request, id=None):
    if id is None:
        raise Http404('No Lookup Provided.')

    obj = get_object_or_404(BlogModel, id=id)
    context = {'obj': obj}
    return render(request, 'core/read_blog.html', context)


def update_one(request, id=None):
    if id is None:
        raise Http404('No Lookup Provided.')

    obj = get_object_or_404(BlogModel, id=id)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=obj)

    context = {'form': form}
    return render(request, 'core/update_blog.html', context)


def delete_one(request, id=None):
    if id is None:
        raise Http404('No Lookup Provided.')

    obj = get_object_or_404(BlogModel, id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('home')

    return render(request, 'core/delete_blog.html')
