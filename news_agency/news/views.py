from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin #UserPassesTestMixin
from django.views.generic import (
    ListView, DetailView, CreateView, 
    DeleteView
    )
from .models import Author, Story

def story(request):
    context = {
        'stories': Story.objects.all()
    }
    return render(request, 'news/home.html', context)

class StoryListView(ListView):
    model = Story
    template_name = 'news/home.html'
    context_object_name = 'stories'
    ordering = ['-story_date']

class StoryDetailView(DetailView):
    model = Story

class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['headline', 'author', 'story_cat',
              'story_region', 'story_details']

def form_valid(self, form):
    form.instance.author = self.request.author
    return super().form_valid(form)

class StoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Story
    success_url = '/'
    
    # def test_func(self):
    #     story = self.get_object()
    #     if self.request.user in self.object.author.all():
    #         return True
    #     return False

def author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'news/author.html', context)
