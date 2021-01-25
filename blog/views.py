from django.shortcuts import render
from .models import Entry
from django.views.generic import ListView, CreateView, DetailView


class HomeView(ListView):
    #this displays the home page
    model = Entry
    template_name = 'index.html'
    context_object_name = 'entries'
    ordering = ['-date'] #arranges posts in this order. - in front of date is for descending order
    paginate_by = 3 #number of posts to display in home page


class EntryDetail(DetailView):
    #this displays the info about a specific object
    model = Entry
    template_name = 'entryDetail.html'


class CreateEntry(CreateView):
    #Form to add more content 
    model = Entry
    template_name = 'createEntry.html'
    fields = ['title', 'text']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
