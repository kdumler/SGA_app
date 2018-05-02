from django.shortcuts import render, redirect
from django import forms
from personal.forms import PostForm
from django.views import generic
from django.views.generic import TemplateView


def contact(request):
    return render(request, 'personal/header.html')


class PostView(TemplateView):
    template_name = 'personal/home.html'
    template_name2 = 'personal/header.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            RSO = form.cleaned_data['RSO']
            Description = form.cleaned_data['Description']
            date = form.cleaned_data['date']

        args = {'form': form}
        return render(request, self.template_name, args)
