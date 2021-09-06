from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup
from datetime import datetime as dt

# Create your views here.
def index(request):
    return HttpResponse("This is the scraper section")


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_statement"] = "This is from the get context method"
        print(context)
        return context

    def say_bye(self):
        return dt.now()
