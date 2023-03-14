from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Index(View):
    def get(self, request):
        return HttpResponse("Welcome To  The Secure Digital Identity System.")
