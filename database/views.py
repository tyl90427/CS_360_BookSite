from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Book

class BookSearchResultsView(ListView):
    model = Book
    template_name = 'home.html'
    object_list = Book.objects.all()

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list
