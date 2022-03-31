from django.shortcuts import render
from bible import models
from django.http import JsonResponse

def index(request):
    book = request.GET.get('book')
    chapter = request.GET.get('chapter')
    verse = request.GET.get('verse')
    content = models.BibleKorhrv.objects.get(book=book, chapter=chapter, verse=verse).content

    return JsonResponse({'content': content})
